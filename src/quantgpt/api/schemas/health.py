"""Health check response schema."""

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Response for GET /health."""

    status: str = Field(..., description="Service status")
    version: str = Field(..., description="API version")
