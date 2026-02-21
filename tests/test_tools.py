"""Tests for agent tools."""

import pytest

from quantgpt.tools import FetchMarketNewsTool, SentimentTool


class TestFetchMarketNewsTool:
    """Tests for FetchMarketNewsTool."""

    def test_execute_returns_non_empty_for_symbol(self) -> None:
        tool = FetchMarketNewsTool()
        result = tool.execute(symbol="AAPL")
        assert isinstance(result, str)
        assert len(result) > 0
        assert "Apple" in result or "iPhone" in result

    def test_execute_returns_non_empty_for_topic(self) -> None:
        tool = FetchMarketNewsTool()
        result = tool.execute(topic="market")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_execute_defaults_to_market_when_empty(self) -> None:
        tool = FetchMarketNewsTool()
        result = tool.execute(symbol="", topic="")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_execute_unknown_symbol_returns_generic_news(self) -> None:
        tool = FetchMarketNewsTool()
        result = tool.execute(symbol="XYZ123")
        assert isinstance(result, str)
        assert len(result) > 0


class TestSentimentTool:
    """Tests for SentimentTool."""

    def test_execute_returns_float_in_range(self) -> None:
        tool = SentimentTool()
        result = tool.execute(text="This is great news for investors!")
        assert isinstance(result, float)
        assert -1 <= result <= 1

    def test_execute_positive_text_returns_positive_score(self) -> None:
        tool = SentimentTool()
        result = tool.execute(text="Amazing growth and excellent performance!")
        assert result > 0

    def test_execute_negative_text_returns_negative_score(self) -> None:
        tool = SentimentTool()
        result = tool.execute(text="Terrible loss and awful decline.")
        assert result < 0

    def test_execute_empty_text_returns_zero(self) -> None:
        tool = SentimentTool()
        result = tool.execute(text="")
        assert result == 0.0
