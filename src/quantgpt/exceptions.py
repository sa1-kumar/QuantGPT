"""QuantGPT exceptions."""


class OllamaUnavailableError(Exception):
    """Raised when Ollama is unreachable or fails."""

    def __init__(self, message: str, cause: Exception | None = None) -> None:
        self.cause = cause
        super().__init__(message)
