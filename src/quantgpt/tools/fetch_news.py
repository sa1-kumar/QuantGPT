"""Fetch market news tool.

Mock implementation for Phase 3. Returns sample news for a given
symbol or topic. Later: integrate NewsAPI, Finnhub, or Alpha Vantage.
"""

from quantgpt.agents.base import BaseTool


# Mock news data for Phase 3
_MOCK_NEWS: dict[str, list[str]] = {
    "aapl": [
        "Apple Inc. reports strong Q4 earnings, beats analyst expectations.",
        "iPhone 16 sales exceed projections in key markets.",
        "Apple announces new AI features for upcoming devices.",
    ],
    "msft": [
        "Microsoft Azure expands cloud services in Asia-Pacific.",
        "Microsoft and OpenAI deepen partnership for AI development.",
        "Windows 11 adoption continues to grow.",
    ],
    "market": [
        "Fed signals potential rate cuts in 2025.",
        "Global markets show mixed signals amid economic data.",
        "Tech sector leads gains as broader market consolidates.",
    ],
}


class FetchMarketNewsTool(BaseTool):
    """Fetches market news for a given symbol or topic."""

    @property
    def name(self) -> str:
        return "fetch_market_news"

    @property
    def description(self) -> str:
        return "Fetches market news for a stock symbol or topic. Use symbol or topic."

    def execute(
        self,
        symbol: str | None = None,
        topic: str | None = None,
        **kwargs: object,
    ) -> str:
        """Fetch market news for symbol or topic.

        Parameters
        ----------
        symbol : str | None
            Stock ticker symbol (e.g. AAPL, MSFT).
        topic : str | None
            News topic (e.g. market, economy).
        **kwargs : object
            Ignored for future extensibility.

        Returns
        -------
        str
            News headlines/snippets as concatenated string.
        """
        key = (symbol or topic or "market").strip().lower()
        if not key:
            key = "market"

        # Try exact match first, then fallback to first word of topic
        if key in _MOCK_NEWS:
            news_items = _MOCK_NEWS[key]
        else:
            # Use first word as symbol for generic lookup, or default
            first_word = key.split()[0] if key else "market"
            news_items = _MOCK_NEWS.get(first_word, _MOCK_NEWS["market"])

        return "\n".join(news_items)
