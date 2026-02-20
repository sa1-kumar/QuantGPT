"""Abstract base classes for agents and tools.

Design: BaseTool (protocol) → BaseAgent (calls tools) → Concrete Agent (implements logic)
Uses dependency injection: tools are passed to agents, not hardcoded.
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """Abstract base for agent tools.

    Tools are pluggable capabilities that agents can invoke.
    Each tool has a name, description, and execute method.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique identifier for the tool."""
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        """Human-readable description for LLM tool selection."""
        ...

    @abstractmethod
    def execute(self, **kwargs: Any) -> Any:
        """Run the tool with given arguments.

        Returns
        -------
        Any
            Tool result (str, dict, number, etc.).
        """
        ...


class BaseAgent(ABC):
    """Abstract base for agents.

    Agents receive tools via dependency injection and implement
    domain-specific logic in run(). Subclasses (Research, Portfolio, Risk)
    extend this and focus on their own logic.
    """

    def __init__(self, tools: list[BaseTool] | None = None) -> None:
        """Initialize agent with optional tools.

        Parameters
        ----------
        tools : list[BaseTool] | None
            Tools the agent can use. Injected, not hardcoded.
        """
        self._tools = {t.name: t for t in (tools or [])}

    @property
    @abstractmethod
    def name(self) -> str:
        """Agent identifier."""
        ...

    @property
    def tools(self) -> list[BaseTool]:
        """List of available tools."""
        return list(self._tools.values())

    def _call_tool(self, tool_name: str, **kwargs: Any) -> Any:
        """Execute a tool by name.

        Parameters
        ----------
        tool_name : str
            Name of the tool to invoke.
        **kwargs : Any
            Arguments passed to the tool's execute().

        Returns
        -------
        Any
            Tool result.

        Raises
        ------
        KeyError
            If tool_name is not found.
        """
        if tool_name not in self._tools:
            raise KeyError(f"Unknown tool: {tool_name}")
        return self._tools[tool_name].execute(**kwargs)

    @abstractmethod
    def run(self, query: str, **kwargs: Any) -> str:
        """Execute the agent's logic for the given query.

        Parameters
        ----------
        query : str
            User or system query.
        **kwargs : Any
            Additional context (e.g., market data, session state).

        Returns
        -------
        str
            Agent response.
        """
        ...
