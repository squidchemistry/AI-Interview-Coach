"""
Configuration utilities for the Project Alpha backend.

This package exposes a single `get_settings` function that returns
an immutable, cached `Settings` instance based on environment variables.
"""

from .settings import Settings, get_settings  # noqa: F401

