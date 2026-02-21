"""Sentiment analysis utilities.

Uses VADER for rule-based sentiment scoring. Works well for
financial/news text without requiring GPU or heavy models.
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

_analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text: str) -> float:
    """Analyze sentiment of given text.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    float
        Sentiment score between -1 and 1.
    """
    if not text or not text.strip():
        return 0.0
    scores = _analyzer.polarity_scores(text)
    # compound score is in [-1, 1], pre-computed by VADER
    return scores["compound"]
