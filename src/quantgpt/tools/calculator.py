"""Calculator tool for basic arithmetic.

Example tool demonstrating the BaseTool protocol.
Used by agents for portfolio calculations, risk metrics, etc.
"""

from quantgpt.agents.base import BaseTool


class CalculatorTool(BaseTool):
    """Performs basic arithmetic operations."""

    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return "Performs add, subtract, multiply, divide. Use operation and two numbers."

    def execute(
        self,
        operation: str,
        a: float,
        b: float,
    ) -> float:
        """Execute arithmetic operation.

        Parameters
        ----------
        operation : str
            One of: add, subtract, multiply, divide
        a : float
            First operand.
        b : float
            Second operand.

        Returns
        -------
        float
            Result of the operation.

        Raises
        ------
        ValueError
            If operation is unknown or division by zero.
        """
        op = operation.lower().strip()
        if op == "add":
            return a + b
        if op == "subtract":
            return a - b
        if op == "multiply":
            return a * b
        if op == "divide":
            if b == 0:
                raise ValueError("Division by zero")
            return a / b
        raise ValueError(f"Unknown operation: {operation}. Use add, subtract, multiply, divide.")
