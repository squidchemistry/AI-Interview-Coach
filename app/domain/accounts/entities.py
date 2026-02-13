from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone

from .exceptions import InvalidEmailError


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class User:
    """
    User aggregate root for the Accounts domain.

    This model captures the core invariants for a user account without
    any persistence or transport concerns.
    """

    id: uuid.UUID
    email: str
    full_name: str
    is_active: bool = True
    created_at: datetime = field(default_factory=_utcnow)
    updated_at: datetime = field(default_factory=_utcnow)

    @staticmethod
    def create(email: str, full_name: str) -> "User":
        normalized_email = email.strip().lower()
        if "@" not in normalized_email:
            raise InvalidEmailError("Email must contain '@'", details={"email": email})

        normalized_name = full_name.strip()
        return User(
            id=uuid.uuid4(),
            email=normalized_email,
            full_name=normalized_name,
        )

    def rename(self, full_name: str) -> None:
        self.full_name = full_name.strip()
        self.touch()

    def deactivate(self) -> None:
        self.is_active = False
        self.touch()

    def touch(self) -> None:
        self.updated_at = _utcnow()

