"""
FastAPI routes for the Interview domain.
"""

from fastapi import APIRouter

from app.application.interview.dto import (
    EvaluationRequest,
    EvaluationResponse,
    QuestionRequest,
    QuestionResponse,
)
from app.application.interview.use_cases import (
    EvaluateAnswerUseCase,
    GenerateQuestionsUseCase,
)
from app.infrastructure.ai.groq_service import GroqAIService


router = APIRouter()


def get_ai_service() -> GroqAIService:
    """
    FastAPI dependency that provides an AIService instance.
    """
    return GroqAIService()


@router.post("/generate-questions", response_model=QuestionResponse)
def generate_questions(
    request: QuestionRequest,
) -> QuestionResponse:
    """
    Generate interview questions for a given role and experience level.
    
    No authentication required - open for trial use.
    """
    ai_service = get_ai_service()
    use_case = GenerateQuestionsUseCase(ai_service)
    result = use_case.execute(request)
    
    if result.is_err:
        raise result.error  # type: ignore[misc]
    
    return result.value  # type: ignore[return-value]


@router.post("/evaluate", response_model=EvaluationResponse)
def evaluate_answer(
    request: EvaluationRequest,
) -> EvaluationResponse:
    """
    Evaluate an interview answer and provide feedback.
    
    No authentication required - open for trial use.
    """
    ai_service = get_ai_service()
    use_case = EvaluateAnswerUseCase(ai_service)
    result = use_case.execute(request)
    
    if result.is_err:
        raise result.error  # type: ignore[misc]
    
    return result.value  # type: ignore[return-value]
