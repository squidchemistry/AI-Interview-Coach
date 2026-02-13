from typing import Optional
from uuid import UUID as UUID_t

from sqlalchemy.orm import Session

from app.application.accounts.interfaces import UserRepository
from app.domain.accounts.entities import User
from app.infrastructure.db.models import UserModel


class SqlAlchemyUserRepository(UserRepository):
    """
    SQLAlchemy implementation of the UserRepository port.
    """

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, user_id: UUID_t) -> Optional[User]:
        row = self._session.get(UserModel, user_id)
        if row is None:
            return None
        return self._to_entity(row)

    def get_by_email(self, email: str) -> Optional[User]:
        row = (
            self._session.query(UserModel)
            .filter(UserModel.email == email.lower())
            .one_or_none()
        )
        if row is None:
            return None
        return self._to_entity(row)

    def add(self, user: User) -> None:
        row = UserModel(
            id=user.id,
            email=user.email,
            full_name=user.full_name,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
        self._session.add(row)
        self._session.commit()

    @staticmethod
    def _to_entity(row: UserModel) -> User:
        return User(
            id=row.id,
            email=row.email,
            full_name=row.full_name,
            is_active=row.is_active,
            created_at=row.created_at,
            updated_at=row.updated_at,
        )

