from fastapi import APIRouter

from .interview import router as interview_router


api_router = APIRouter()

# Group routes by business capability (domain).
api_router.include_router(interview_router, prefix="/interview", tags=["interview"])

