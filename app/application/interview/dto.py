"""
Data Transfer Objects for the Interview domain.
"""

from pydantic import BaseModel


class QuestionRequest(BaseModel):
    """Request DTO for generating interview questions."""

    role: str
    experience: str


class QuestionResponse(BaseModel):
    """Response DTO for interview questions."""

    questions: list[str]


class EvaluationRequest(BaseModel):
    """Request DTO for evaluating an interview answer."""

    question: str
    answer: str


class EvaluationResponse(BaseModel):
    """Response DTO for interview evaluation."""

    score: int
    strengths: list[str]
    weaknesses: list[str]
    improved_answer: str
