"""Models routes."""

from fastapi import APIRouter, Depends

from quantgpt.api.config import ModelInfo, get_available_models
from quantgpt.api.schemas.models import ModelInfoSchema, ModelsResponse

router = APIRouter(prefix="/api/v1", tags=["models"])


def _model_info_to_schema(m: ModelInfo) -> ModelInfoSchema:
    """Convert config ModelInfo to response schema."""
    return ModelInfoSchema(id=m.id, name=m.name, provider=m.provider)


@router.get("/models", response_model=ModelsResponse)
def list_models(
    models: list[ModelInfo] = Depends(get_available_models),
) -> ModelsResponse:
    """List available LLM models from config."""
    return ModelsResponse(models=[_model_info_to_schema(m) for m in models])
