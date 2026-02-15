"""Basic import tests for QuantGPT."""


def test_imports() -> None:
    import quantgpt
    import quantgpt.nlp
    import quantgpt.forecasting
    import quantgpt.portfolio
    import quantgpt.dashboard
    import quantgpt.agents
    import quantgpt.tools
    import quantgpt.api

    assert hasattr(quantgpt, "nlp")
    assert hasattr(quantgpt, "forecasting")
    assert hasattr(quantgpt, "portfolio")
    assert hasattr(quantgpt, "dashboard")
    assert hasattr(quantgpt, "agents")
    assert hasattr(quantgpt, "tools")
    assert hasattr(quantgpt, "api")
