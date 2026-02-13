"""
Domain entities for the Interview domain.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class InterviewQuestion:
    """Domain entity representing an interview question."""

    question: str
    role: str
    experience_level: str

    def __post_init__(self) -> None:
        """Validate domain invariants."""
        if not self.question or not self.question.strip():
            raise ValueError("Question cannot be empty")
        if not self.role or not self.role.strip():
            raise ValueError("Role cannot be empty")


@dataclass
class InterviewEvaluation:
    """Domain entity representing an interview answer evaluation."""

    score: int
    strengths: list[str]
    weaknesses: list[str]
    improved_answer: str

    def __post_init__(self) -> None:
        """Validate domain invariants."""
        if not (1 <= self.score <= 10):
            raise ValueError("Score must be between 1 and 10")
        if not isinstance(self.strengths, list):
            raise ValueError("Strengths must be a list")
        if not isinstance(self.weaknesses, list):
            raise ValueError("Weaknesses must be a list")
