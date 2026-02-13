from uuid import UUID

from app.application.accounts.dto import RegisterUserInput, UserOutput
from app.application.accounts.interfaces import UserRepository
from app.domain.accounts.entities import User
from app.domain.accounts.exceptions import UserAlreadyExistsError, UserNotFoundError
from app.shared.result import Result


class RegisterUserUseCase:
    """
    Use case: register a new user account.
    """

    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo

    def execute(self, data: RegisterUserInput) -> Result[User]:
        existing = self._repo.get_by_email(str(data.email))
        if existing is not None:
            return Result.err(
                UserAlreadyExistsError(
                    "A user with this email already exists",
                    details={"email": str(data.email)},
                )
            )

        user = User.create(email=str(data.email), full_name=data.full_name)
        user.is_active = data.is_active
        self._repo.add(user)

        return Result.ok(user)


class GetUserByIdUseCase:
    """
    Use case: fetch a user by ID.
    """

    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo

    def execute(self, user_id: UUID) -> Result[User]:
        user = self._repo.get_by_id(user_id)
        if user is None:
            return Result.err(
                UserNotFoundError(
                    "User not found",
                    details={"user_id": str(user_id)},
                )
            )
        return Result.ok(user)

