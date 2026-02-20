"""Tests for FastAPI endpoints."""

import pytest
from fastapi.testclient import TestClient

from quantgpt.api.main import create_app


@pytest.fixture
def client() -> TestClient:
    """Create test client with overridden dependencies."""
    return TestClient(create_app())


class TestHealth:
    """Tests for GET /health."""

    def test_health_returns_ok(self, client: TestClient) -> None:
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "version" in data

    def test_health_response_schema(self, client: TestClient) -> None:
        response = client.get("/health")
        data = response.json()
        assert isinstance(data["status"], str)
        assert isinstance(data["version"], str)


class TestModels:
    """Tests for GET /api/v1/models."""

    def test_models_returns_list(self, client: TestClient) -> None:
        response = client.get("/api/v1/models")
        assert response.status_code == 200
        data = response.json()
        assert "models" in data
        assert isinstance(data["models"], list)

    def test_models_contain_expected_fields(self, client: TestClient) -> None:
        response = client.get("/api/v1/models")
        data = response.json()
        assert len(data["models"]) >= 1
        for model in data["models"]:
            assert "id" in model
            assert "name" in model
            assert "provider" in model

    def test_models_include_ollama(self, client: TestClient) -> None:
        response = client.get("/api/v1/models")
        data = response.json()
        providers = [m["provider"] for m in data["models"]]
        assert "ollama" in providers


class TestOpenAPI:
    """Tests for OpenAPI docs."""

    def test_openapi_json_available(self, client: TestClient) -> None:
        response = client.get("/openapi.json")
        assert response.status_code == 200
        spec = response.json()
        assert "openapi" in spec
        assert "paths" in spec

    def test_health_in_openapi(self, client: TestClient) -> None:
        response = client.get("/openapi.json")
        spec = response.json()
        assert "/health" in spec["paths"]

    def test_models_in_openapi(self, client: TestClient) -> None:
        response = client.get("/openapi.json")
        spec = response.json()
        assert "/api/v1/models" in spec["paths"]
