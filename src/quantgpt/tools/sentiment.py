"""Sentiment analysis tool.

Wraps quantgpt.nlp.analyze_sentiment for use in agent workflows.
"""

from quantgpt.agents.base import BaseTool
from quantgpt.nlp import analyze_sentiment


class SentimentTool(BaseTool):
    """Analyzes sentiment of text; returns score between -1 and 1."""

    @property
    def name(self) -> str:
        return "analyze_sentiment"

    @property
    def description(self) -> str:
        return "Analyzes sentiment of text; returns score -1 to 1 (negative to positive)."

    def execute(self, text: str, **kwargs: object) -> float:
        """Analyze sentiment of given text.

        Parameters
        ----------
        text : str
            Input text to analyze.
        **kwargs : object
            Ignored for future extensibility.

        Returns
        -------
        float
            Sentiment score between -1 and 1.
        """
        return analyze_sentiment(text)
