"""Research routes."""

from fastapi import APIRouter, Depends, HTTPException

from quantgpt.agents import ResearchAgent
from quantgpt.api.config import get_ollama_base_url, get_ollama_model
from quantgpt.api.schemas.research import ResearchRequest, ResearchResponse
from quantgpt.exceptions import OllamaUnavailableError

router = APIRouter(prefix="/api/v1", tags=["research"])


def get_research_agent() -> ResearchAgent:
    """Dependency: create ResearchAgent with config."""
    return ResearchAgent(
        ollama_base_url=get_ollama_base_url(),
        ollama_model=get_ollama_model(),
    )


@router.post("/research", response_model=ResearchResponse)
def run_research(
    body: ResearchRequest,
    agent: ResearchAgent = Depends(get_research_agent),
) -> ResearchResponse:
    """Run research agent on the given query. Returns investment insight."""
    try:
        insight = agent.run(body.query)
    except OllamaUnavailableError as e:
        raise HTTPException(
            status_code=503,
            detail="Ollama is not available. Start with: ollama serve. Then: ollama pull llama3.2",
        ) from e
    return ResearchResponse(insight=insight)
