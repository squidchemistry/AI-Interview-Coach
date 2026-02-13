from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.shared.errors import AppError


def register_error_handlers(app: FastAPI) -> None:
    """
    Register global exception handlers for application-specific errors.
    """

    @app.exception_handler(AppError)
    async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:  # type: ignore[unused-ignore]
        return JSONResponse(status_code=exc.status_code, content=exc.to_dict())

