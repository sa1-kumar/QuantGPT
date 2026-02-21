"""Tests for ResearchAgent and POST /api/v1/research."""

import pytest
from fastapi.testclient import TestClient

from quantgpt.agents import ResearchAgent
from quantgpt.api.main import create_app
from quantgpt.exceptions import OllamaUnavailableError


class TestResearchAgent:
    """Unit tests for ResearchAgent."""

    def test_run_raises_when_ollama_unavailable(self) -> None:
        """Test that run() raises OllamaUnavailableError when Ollama is unreachable."""
        agent = ResearchAgent(
            ollama_base_url="http://invalid:9999",
            ollama_model="llama3.2",
        )
        with pytest.raises(OllamaUnavailableError):
            agent.run("AAPL")

    def test_run_returns_string_when_ollama_available(self) -> None:
        """Test that run() returns insight when Ollama works (may skip if Ollama not running)."""
        agent = ResearchAgent(
            ollama_base_url="http://localhost:11434",
            ollama_model="llama3.2",
        )
        try:
            result = agent.run("market")
            assert isinstance(result, str)
            assert len(result) > 0
        except OllamaUnavailableError:
            pytest.skip("Ollama not running")


class TestResearchEndpoint:
    """Integration tests for POST /api/v1/research."""

    def test_research_returns_200_with_mock_agent(self) -> None:
        """Test POST /api/v1/research returns 200 and insight when agent succeeds."""
        class MockResearchAgent:
            def run(self, query: str, **kwargs: object) -> str:
                return "Mock insight for testing."

        def mock_agent() -> MockResearchAgent:
            return MockResearchAgent()

        app = create_app()
        from quantgpt.api.routes.research import get_research_agent

        app.dependency_overrides[get_research_agent] = mock_agent

        client = TestClient(app)
        response = client.post("/api/v1/research", json={"query": "AAPL"})
        assert response.status_code == 200
        data = response.json()
        assert data["insight"] == "Mock insight for testing."

    def test_research_returns_503_when_ollama_unavailable(self) -> None:
        """Test POST /api/v1/research returns 503 when Ollama is unreachable."""
        def mock_agent() -> ResearchAgent:
            return ResearchAgent(
                ollama_base_url="http://invalid-ollama:9999",
                ollama_model="llama3.2",
            )

        app = create_app()
        from quantgpt.api.routes.research import get_research_agent

        app.dependency_overrides[get_research_agent] = mock_agent

        client = TestClient(app)
        response = client.post("/api/v1/research", json={"query": "AAPL"})
        assert response.status_code == 503
        data = response.json()
        assert "detail" in data
        assert "Ollama" in data["detail"]

    def test_research_endpoint_validates_request(self) -> None:
        """Test POST /api/v1/research rejects missing query."""
        client = TestClient(create_app())
        response = client.post("/api/v1/research", json={})
        assert response.status_code == 422

    def test_research_in_openapi(self) -> None:
        """Test /api/v1/research is in OpenAPI spec."""
        client = TestClient(create_app())
        response = client.get("/openapi.json")
        spec = response.json()
        assert "/api/v1/research" in spec["paths"]
        assert "post" in spec["paths"]["/api/v1/research"]
