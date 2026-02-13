from fastapi import APIRouter

from .accounts import router as accounts_router


api_router = APIRouter()

# Group routes by business capability (domain).
api_router.include_router(accounts_router, prefix="/accounts", tags=["accounts"])

