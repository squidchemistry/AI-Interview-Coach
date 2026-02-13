"""
Domain model for the Accounts bounded context.

Includes the `User` aggregate and related domain-specific exceptions.
"""

from .entities import User  # noqa: F401
from . import exceptions as exceptions  # noqa: F401

