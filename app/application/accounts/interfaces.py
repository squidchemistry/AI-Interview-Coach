from typing import Optional, Protocol
from uuid import UUID

from app.domain.accounts.entities import User


class UserRepository(Protocol):
    """
    Port for user persistence operations.
    """

    def get_by_id(self, user_id: UUID) -> Optional[User]:
        ...

    def get_by_email(self, email: str) -> Optional[User]:
        ...

    def add(self, user: User) -> None:
        ...

