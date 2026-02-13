"""
API layer for the Project Alpha backend.

This package contains:
- FastAPI routers grouped by domain.
- Error handlers that map domain/app errors to HTTP responses.
"""

from .routes import api_router  # noqa: F401
from .error_handlers import register_error_handlers  # noqa: F401

