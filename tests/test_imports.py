"""Basic import tests for QuantGPT."""


def test_imports() -> None:
    import quantgpt
    import quantgpt.nlp
    import quantgpt.forecasting
    import quantgpt.portfolio
    import quantgpt.dashboard

    assert hasattr(quantgpt, "nlp")
    assert hasattr(quantgpt, "forecasting")
    assert hasattr(quantgpt, "portfolio")
    assert hasattr(quantgpt, "dashboard")
