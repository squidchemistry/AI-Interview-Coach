from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.infrastructure.config.settings import get_settings


Base = declarative_base()


def _get_engine():
    settings = get_settings()
    return create_engine(settings.database_url, future=True)


engine = _get_engine()
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=Session,
)


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency that yields a database session.
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

