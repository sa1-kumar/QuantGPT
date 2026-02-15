"""API configuration.

Models and settings for the API. Uses dependency injection
via FastAPI's Depends() for testability.
"""

from dataclasses import dataclass


@dataclass
class ModelInfo:
    """LLM model metadata."""

    id: str
    name: str
    provider: str


def get_available_models() -> list[ModelInfo]:
    """Return available LLM models from config.

    In Phase 2 this is static. Later: env vars, config file, or registry.
    """
    return [
        ModelInfo(id="llama3.2", name="Llama 3.2", provider="ollama"),
        ModelInfo(id="mistral", name="Mistral", provider="ollama"),
    ]
