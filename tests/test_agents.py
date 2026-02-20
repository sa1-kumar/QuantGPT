"""Tests for agent base classes and concrete agents."""

import pytest

from quantgpt.agents.base import BaseAgent, BaseTool
from quantgpt.agents.math_agent import MathAgent
from quantgpt.tools.calculator import CalculatorTool


class TestBaseTool:
    """Tests for BaseTool ABC."""

    def test_cannot_instantiate_base_tool(self) -> None:
        with pytest.raises(TypeError):
            BaseTool()  # type: ignore[abstract]

    def test_calculator_is_base_tool(self) -> None:
        tool = CalculatorTool()
        assert isinstance(tool, BaseTool)


class TestBaseAgent:
    """Tests for BaseAgent ABC."""

    def test_cannot_instantiate_base_agent(self) -> None:
        with pytest.raises(TypeError):
            BaseAgent()  # type: ignore[abstract]

    def test_agent_receives_tools_via_injection(self) -> None:
        tool = CalculatorTool()
        agent = MathAgent(tools=[tool])
        assert len(agent.tools) == 1
        assert agent.tools[0].name == "calculator"

    def test_call_tool_unknown_raises(self) -> None:
        agent = MathAgent(tools=[])
        with pytest.raises(KeyError, match="Unknown tool"):
            agent._call_tool("nonexistent", x=1)


class TestMathAgent:
    """Tests for MathAgent (concrete BaseAgent implementation)."""

    def test_name(self) -> None:
        agent = MathAgent()
        assert agent.name == "math_agent"

    def test_run_add(self) -> None:
        agent = MathAgent()
        assert agent.run("add 2 3") == "5.0"

    def test_run_subtract(self) -> None:
        agent = MathAgent()
        assert agent.run("subtract 10 4") == "6.0"

    def test_run_multiply(self) -> None:
        agent = MathAgent()
        assert agent.run("multiply 3 4") == "12.0"

    def test_run_divide(self) -> None:
        agent = MathAgent()
        assert agent.run("divide 15 3") == "5.0"

    def test_run_invalid_query_returns_usage(self) -> None:
        agent = MathAgent()
        result = agent.run("invalid")
        assert "Usage" in result or "usage" in result.lower()

    def test_run_invalid_numbers_returns_message(self) -> None:
        agent = MathAgent()
        result = agent.run("add foo bar")
        assert "invalid" in result.lower() or "numeric" in result.lower()

    def test_run_division_by_zero(self) -> None:
        agent = MathAgent()
        with pytest.raises(ValueError, match="Division by zero"):
            agent.run("divide 1 0")
