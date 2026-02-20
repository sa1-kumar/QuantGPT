"""Models endpoint response schemas."""

from pydantic import BaseModel, Field


class ModelInfoSchema(BaseModel):
    """Single model metadata."""

    id: str = Field(..., description="Model identifier")
    name: str = Field(..., description="Display name")
    provider: str = Field(..., description="Provider (e.g. ollama)")


class ModelsResponse(BaseModel):
    """Response for GET /api/v1/models."""

    models: list[ModelInfoSchema] = Field(..., description="Available models")
