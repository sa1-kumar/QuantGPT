"""FastAPI application factory.

Uses create_app() for testability and dependency injection.
OpenAPI docs at /docs, spec at /openapi.json.
"""

from fastapi import FastAPI

from quantgpt.api.routes import health, models, research

__version__ = "0.1.0"


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="QuantGPT API",
        description="AI-powered investment advisor API",
        version=__version__,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    app.include_router(health.router)
    app.include_router(models.router)
    app.include_router(research.router)

    return app


app = create_app()


def run() -> None:
    """Run the API server. Entry point for quantgpt-api CLI."""
    import uvicorn

    uvicorn.run(
        "quantgpt.api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
