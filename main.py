from fastapi import FastAPI

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
    """
    settings = get_settings()
    configure_logging(settings)

    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        docs_url="/docs" if settings.enable_docs else None,
        redoc_url="/redoc" if settings.enable_docs else None,
    )

    # Include versioned API router
    app.include_router(api_router, prefix="/v1")

    # Register centralized error handlers
    register_error_handlers(app)

    return app


app = create_app()

