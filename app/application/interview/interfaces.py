"""
Ports (interfaces) for the Interview domain.

These define contracts that infrastructure must implement.
"""

from typing import Protocol

from app.domain.interview.entities import InterviewEvaluation, InterviewQuestion


class AIService(Protocol):
    """
    Port for AI/LLM service operations.
    """

    def generate_questions(self, role: str, experience: str) -> list[str]:
        """Generate interview questions for a given role and experience level."""
        ...

    def evaluate_answer(self, question: str, answer: str) -> InterviewEvaluation:
        """Evaluate an interview answer and provide feedback."""
        ...
