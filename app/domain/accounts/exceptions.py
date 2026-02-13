from app.shared.errors import ConflictError, DomainError, NotFoundError


class InvalidEmailError(DomainError):
    code = "invalid_email"


class UserAlreadyExistsError(ConflictError):
    code = "user_already_exists"


class UserNotFoundError(NotFoundError):
    code = "user_not_found"

