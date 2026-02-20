"""Tests for agent tools."""

import pytest

from quantgpt.tools.calculator import CalculatorTool


class TestCalculatorTool:
    """Tests for CalculatorTool."""

    def test_name(self) -> None:
        tool = CalculatorTool()
        assert tool.name == "calculator"

    def test_description(self) -> None:
        tool = CalculatorTool()
        assert "add" in tool.description.lower()
        assert "subtract" in tool.description.lower()

    def test_add(self) -> None:
        tool = CalculatorTool()
        assert tool.execute(operation="add", a=2.0, b=3.0) == 5.0

    def test_subtract(self) -> None:
        tool = CalculatorTool()
        assert tool.execute(operation="subtract", a=10.0, b=4.0) == 6.0

    def test_multiply(self) -> None:
        tool = CalculatorTool()
        assert tool.execute(operation="multiply", a=3.0, b=4.0) == 12.0

    def test_divide(self) -> None:
        tool = CalculatorTool()
        assert tool.execute(operation="divide", a=15.0, b=3.0) == 5.0

    def test_divide_by_zero_raises(self) -> None:
        tool = CalculatorTool()
        with pytest.raises(ValueError, match="Division by zero"):
            tool.execute(operation="divide", a=1.0, b=0.0)

    def test_unknown_operation_raises(self) -> None:
        tool = CalculatorTool()
        with pytest.raises(ValueError, match="Unknown operation"):
            tool.execute(operation="modulo", a=5.0, b=2.0)

    def test_operation_case_insensitive(self) -> None:
        tool = CalculatorTool()
        assert tool.execute(operation="ADD", a=1.0, b=2.0) == 3.0
