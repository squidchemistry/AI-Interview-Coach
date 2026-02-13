from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings


Environment = Literal["development", "staging", "production", "test"]


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables (and optional .env).

    This object is used across the app to avoid scattering direct
    environment access. It can be extended as new concerns appear
    (e.g. caching, messaging, feature flags).
    """

    app_name: str = Field(default="Project Alpha Backend", alias="APP_NAME")
    environment: Environment = Field(default="development", alias="APP_ENV")
    version: str = Field(default="0.1.0", alias="APP_VERSION")
    enable_docs: bool = Field(default=True, alias="ENABLE_DOCS")

    database_url: str = Field(
        default="postgresql+psycopg2://user:password@localhost:5432/project_alpha",
        alias="DATABASE_URL",
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached Settings instance.

    Using an LRU cache ensures environment variables are loaded once per process,
    which keeps configuration access fast and predictable.
    """

    return Settings()

