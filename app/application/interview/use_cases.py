"""
Use cases for the Interview domain.
"""

from app.application.interview.dto import (
    EvaluationRequest,
    EvaluationResponse,
    QuestionRequest,
    QuestionResponse,
)
from app.application.interview.interfaces import AIService
from app.domain.interview.entities import InterviewEvaluation, InterviewQuestion
from app.shared.errors import InfrastructureError
from app.shared.result import Result


class GenerateQuestionsUseCase:
    """
    Use case: generate interview questions for a role and experience level.
    """

    def __init__(self, ai_service: AIService) -> None:
        self._ai_service = ai_service

    def execute(self, request: QuestionRequest) -> Result[QuestionResponse]:
        """
        Generate interview questions.

        Args:
            request: Contains role and experience level

        Returns:
            Result containing list of questions or an error
        """
        try:
            questions = self._ai_service.generate_questions(
                role=request.role, experience=request.experience
            )
            return Result.ok(QuestionResponse(questions=questions))
        except Exception as e:
            return Result.err(
                InfrastructureError(
                    "Failed to generate questions",
                    details={"error": str(e)},
                )
            )


class EvaluateAnswerUseCase:
    """
    Use case: evaluate an interview answer.
    """

    def __init__(self, ai_service: AIService) -> None:
        self._ai_service = ai_service

    def execute(self, request: EvaluationRequest) -> Result[EvaluationResponse]:
        """
        Evaluate an interview answer.

        Args:
            request: Contains question and answer

        Returns:
            Result containing evaluation (score, strengths, weaknesses, improved_answer)
        """
        try:
            evaluation = self._ai_service.evaluate_answer(
                question=request.question, answer=request.answer
            )
            return Result.ok(
                EvaluationResponse(
                    score=evaluation.score,
                    strengths=evaluation.strengths,
                    weaknesses=evaluation.weaknesses,
                    improved_answer=evaluation.improved_answer,
                )
            )
        except Exception as e:
            return Result.err(
                InfrastructureError(
                    "Failed to evaluate answer",
                    details={"error": str(e)},
                )
            )
