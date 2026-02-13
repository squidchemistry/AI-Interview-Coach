from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.domain.accounts.entities import User


class RegisterUserInput(BaseModel):
    email: EmailStr
    full_name: str
    is_active: bool = True


class UserOutput(BaseModel):
    id: UUID
    email: EmailStr
    full_name: str
    is_active: bool

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(user: User) -> "UserOutput":
        return UserOutput(
            id=user.id,
            email=user.email,
            full_name=user.full_name,
            is_active=user.is_active,
        )

