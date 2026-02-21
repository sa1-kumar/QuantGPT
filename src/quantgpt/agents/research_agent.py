"""Research agent using LangGraph.

3-node workflow: fetch_news -> analyze_sentiment -> llm_summarize.
Produces investment insight from market news and sentiment.
"""

from typing import TypedDict

from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph

from quantgpt.exceptions import OllamaUnavailableError
from quantgpt.tools.fetch_news import FetchMarketNewsTool
from quantgpt.tools.sentiment import SentimentTool


class ResearchState(TypedDict, total=False):
    """State schema for ResearchAgent graph."""

    query: str
    news: str
    sentiment_score: float
    insight: str


class ResearchAgent:
    """Research agent with LangGraph: fetch news, analyze sentiment, LLM summarize."""

    def __init__(
        self,
        ollama_base_url: str = "http://localhost:11434",
        ollama_model: str = "llama3.2",
    ) -> None:
        """Initialize ResearchAgent.

        Parameters
        ----------
        ollama_base_url : str
            Ollama API base URL.
        ollama_model : str
            Ollama model name (e.g. llama3.2, mistral).
        """
        self._ollama_base_url = ollama_base_url
        self._ollama_model = ollama_model
        self._fetch_news = FetchMarketNewsTool()
        self._sentiment = SentimentTool()
        self._graph = self._build_graph()

    def _build_graph(self):
        """Build and compile the LangGraph state machine."""
        graph = StateGraph(ResearchState)

        graph.add_node("fetch_news", self._fetch_news_node)
        graph.add_node("analyze_sentiment", self._analyze_sentiment_node)
        graph.add_node("llm_summarize", self._llm_summarize_node)

        graph.add_edge(START, "fetch_news")
        graph.add_edge("fetch_news", "analyze_sentiment")
        graph.add_edge("analyze_sentiment", "llm_summarize")
        graph.add_edge("llm_summarize", END)

        return graph.compile()

    def _fetch_news_node(self, state: ResearchState) -> dict[str, str]:
        """Node 1: Fetch market news for the query."""
        query = state.get("query", "") or "market"
        topic = query.strip() or "market"
        news = self._fetch_news.execute(symbol=None, topic=topic)
        return {"news": news}

    def _analyze_sentiment_node(self, state: ResearchState) -> dict[str, float]:
        """Node 2: Analyze sentiment of fetched news."""
        news = state.get("news", "") or ""
        score = self._sentiment.execute(text=news)
        return {"sentiment_score": score}

    def _llm_summarize_node(self, state: ResearchState) -> dict[str, str]:
        """Node 3: LLM summarizes news and sentiment into investment insight."""
        news = state.get("news", "")
        sentiment = state.get("sentiment_score", 0.0)
        prompt = (
            f"Given this market news and sentiment score ({sentiment:.2f}, range -1 to 1):\n\n"
            f"News:\n{news}\n\n"
            "Provide a brief investment insight (2-3 sentences). Be concise."
        )
        try:
            llm = ChatOllama(
                model=self._ollama_model,
                base_url=self._ollama_base_url,
            )
            response = llm.invoke(prompt)
            insight = response.content if hasattr(response, "content") else str(response)
        except Exception as e:
            raise OllamaUnavailableError(
                "Ollama not available. Start with: ollama serve. Then: ollama pull llama3.2",
                cause=e,
            ) from e
        return {"insight": insight}

    def run(self, query: str, **kwargs: object) -> str:
        """Execute the research agent for the given query.

        Parameters
        ----------
        query : str
            User query (symbol, topic, or research question).
        **kwargs : object
            Ignored for future extensibility.

        Returns
        -------
        str
            Investment insight from the agent.
        """
        initial: ResearchState = {"query": query}
        final = self._graph.invoke(initial)
        return final.get("insight", "")
