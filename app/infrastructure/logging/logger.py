import logging
from logging.config import dictConfig

from app.infrastructure.config.settings import Settings


def configure_logging(settings: Settings) -> None:
    """
    Configure application-wide logging.

    This uses a simple, structured-friendly format and can be extended
    later to integrate with centralized logging solutions.
    """

    level = logging.INFO if settings.environment != "production" else logging.WARNING

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": (
                        "%(asctime)s %(levelname)s [%(name)s] "
                        "%(message)s "
                        "(correlation_id=%(correlation_id)s)"
                    ),
                },
            },
            "filters": {
                "correlation": {
                    "()": "logging.Filter",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                },
            },
            "root": {
                "level": level,
                "handlers": ["console"],
            },
        }
    )


def get_logger(name: str) -> logging.Logger:
    """
    Convenience helper to get a logger with the configured settings applied.
    """

    logger = logging.getLogger(name)
    # Ensure correlation_id attribute exists to satisfy formatter.
    if not hasattr(logger, "correlation_id"):
        # Logging records will pick this up via `extra` in practice.
        logger.correlation_id = "-"  # type: ignore[attr-defined]
    return logger

