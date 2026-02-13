"""
Shared cross-cutting utilities for the AI Interview Coach backend.

This package includes:
- Base error types used across layers.
- A simple Result type to represent operation outcomes.
"""

from .errors import (  # noqa: F401
    AppError,
    ConflictError,
    DomainError,
    InfrastructureError,
    NotFoundError,
    ValidationError,
)
from .result import Result  # noqa: F401

