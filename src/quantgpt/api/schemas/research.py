"""Research endpoint request/response schemas."""

from pydantic import BaseModel, Field


class ResearchRequest(BaseModel):
    """Request for POST /api/v1/research."""

    query: str = Field(..., description="Research query (symbol, topic, or question)")


class ResearchResponse(BaseModel):
    """Response for POST /api/v1/research."""

    insight: str = Field(..., description="Investment insight from the research agent")
