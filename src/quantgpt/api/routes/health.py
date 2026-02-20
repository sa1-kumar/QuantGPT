"""Health check routes."""

from fastapi import APIRouter

from quantgpt.api.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def get_health() -> HealthResponse:
    """Liveness probe. Returns service status and version."""
    return HealthResponse(status="ok", version="0.1.0")
