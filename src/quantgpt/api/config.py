"""API configuration.

Models and settings for the API. Uses dependency injection
via FastAPI's Depends() for testability.
"""

import os
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


def get_ollama_base_url() -> str:
    """Return Ollama API base URL. Reads from OLLAMA_BASE_URL env."""
    return os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")


def get_ollama_model() -> str:
    """Return Ollama model name. Reads from OLLAMA_MODEL env."""
    return os.environ.get("OLLAMA_MODEL", "llama3.2")
