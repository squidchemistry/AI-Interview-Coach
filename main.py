from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.api.error_handlers import register_error_handlers
from app.api.routes import api_router
from app.infrastructure.config.settings import get_settings
from app.infrastructure.logging.logger import configure_logging


def create_app() -> FastAPI:
    """
    Application factory for the FastAPI app.

    This wires together:
    - Settings and logging configuration.
    - API routers.
    - Global exception handlers.
    - CORS middleware for frontend integration.
    """
    settings = get_settings()
    configure_logging(settings)

    app = FastAPI(
        title="AI Interview Coach",
        version=settings.version,
        docs_url="/docs" if settings.enable_docs else None,
        redoc_url="/redoc" if settings.enable_docs else None,
    )

    # Enable CORS for React frontend
    cors_origins = settings.cors_origins.split(",") if settings.cors_origins else []
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Health check endpoint (before static files)
    @app.get("/ping")
    def ping():
        """Health check endpoint."""
        return {"status": "alive"}

    # Include versioned API router
    app.include_router(api_router, prefix="/v1")

    # Register centralized error handlers
    register_error_handlers(app)

    # Serve static files (frontend) in production - mount last to avoid conflicts
    static_dir = Path(__file__).parent / "static"
    if static_dir.exists():
        # Mount static files, but exclude API routes
        app.mount("/", StaticFiles(directory=str(static_dir), html=True), name="static")

    return app


app = create_app()

