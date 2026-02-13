from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.application.accounts.dto import RegisterUserInput, UserOutput
from app.application.accounts.interfaces import UserRepository
from app.application.accounts.use_cases import GetUserByIdUseCase, RegisterUserUseCase
from app.infrastructure.db.repositories import SqlAlchemyUserRepository
from app.infrastructure.db.session import get_db


router = APIRouter()


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    """
    FastAPI dependency that provides a UserRepository instance.
    """

    return SqlAlchemyUserRepository(db)


@router.post("/users", response_model=UserOutput, status_code=201)
def register_user(
    payload: RegisterUserInput,
    repo: UserRepository = Depends(get_user_repository),
) -> UserOutput:
    """
    Register a new user account.
    """

    use_case = RegisterUserUseCase(repo)
    result = use_case.execute(payload)
    if result.is_err:
        # Propagate AppError subclasses to be handled centrally.
        raise result.error  # type: ignore[misc]
    return UserOutput.from_entity(result.value)  # type: ignore[arg-type]


@router.get("/users/{user_id}", response_model=UserOutput)
def get_user(
    user_id: UUID,
    repo: UserRepository = Depends(get_user_repository),
) -> UserOutput:
    """
    Fetch a user by ID.
    """

    use_case = GetUserByIdUseCase(repo)
    result = use_case.execute(user_id)
    if result.is_err:
        raise result.error  # type: ignore[misc]
    return UserOutput.from_entity(result.value)  # type: ignore[arg-type]

