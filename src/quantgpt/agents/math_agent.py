"""Minimal concrete agent for Phase 1 scaffolding.

Demonstrates BaseAgent + BaseTool flow. Uses CalculatorTool
to answer simple arithmetic queries. Will be replaced by
specialist agents (Research, Portfolio, Risk) in later phases.
"""

from typing import Any

from quantgpt.agents.base import BaseAgent, BaseTool
from quantgpt.tools.calculator import CalculatorTool


class MathAgent(BaseAgent):
    """Simple agent that uses CalculatorTool for arithmetic."""

    def __init__(self, tools: list[BaseTool] | None = None) -> None:
        default_tools = [CalculatorTool()] if tools is None else tools
        super().__init__(tools=default_tools)

    @property
    def name(self) -> str:
        return "math_agent"

    def run(self, query: str, **kwargs: Any) -> str:
        """Parse simple 'op a b' queries and return result."""
        parts = query.strip().lower().split()
        if len(parts) != 3:
            return "Usage: <operation> <number> <number> (e.g. add 2 3)"
        op, a_str, b_str = parts
        try:
            a, b = float(a_str), float(b_str)
        except ValueError:
            return "Invalid numbers. Use numeric values."
        result = self._call_tool("calculator", operation=op, a=a, b=b)
        return str(result)