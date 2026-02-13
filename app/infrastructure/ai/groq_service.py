"""
Groq AI service implementation.
"""

import json
import os
from typing import Optional

from groq import Groq

from app.application.interview.interfaces import AIService
from app.domain.interview.entities import InterviewEvaluation
from app.shared.errors import InfrastructureError


class GroqAIService(AIService):
    """
    Groq API implementation of the AIService port.
    """

    def __init__(self, api_key: Optional[str] = None) -> None:
        """
        Initialize Groq client.

        Args:
            api_key: Groq API key. If not provided, reads from GROQ_API_KEY env var.
        """
        api_key = api_key or os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is required")
        self._client = Groq(api_key=api_key)
        self._model = "llama-3.1-8b-instant"

    def generate_questions(self, role: str, experience: str) -> list[str]:
        """
        Generate interview questions using Groq API.

        Args:
            role: Job role (e.g., "Software Engineer")
            experience: Experience level (e.g., "2 years")

        Returns:
            List of interview questions

        Raises:
            InfrastructureError: If API call fails
        """
        try:
            prompt = f"""
            Generate 5 realistic technical interview questions 
            for a {role} with {experience} of experience.
            Return a JSON object with a key "questions" containing a list of strings.
            Output ONLY the raw JSON.
            """

            response = self._client.chat.completions.create(
                model=self._model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                response_format={"type": "json_object"},
            )

            content = response.choices[0].message.content
            if not content:
                raise InfrastructureError("Empty response from AI service")

            data = json.loads(content)
            questions = data.get("questions", [])
            if not questions:
                raise InfrastructureError("No questions returned from AI service")

            return questions

        except json.JSONDecodeError as e:
            raise InfrastructureError(
                "Invalid JSON response from AI service",
                details={"error": str(e)},
            )
        except Exception as e:
            raise InfrastructureError(
                "Failed to generate questions",
                details={"error": str(e)},
            )

    def evaluate_answer(self, question: str, answer: str) -> InterviewEvaluation:
        """
        Evaluate an interview answer using Groq API.

        Args:
            question: The interview question
            answer: The candidate's answer

        Returns:
            InterviewEvaluation with score, strengths, weaknesses, and improved answer

        Raises:
            InfrastructureError: If API call fails
        """
        try:
            prompt = f"""
            You are an expert technical interviewer.
            
            Question: {question}
            Candidate Answer: {answer}

            Provide a JSON object with the following keys:
            - "score": integer (1-10)
            - "strengths": list of strings
            - "weaknesses": list of strings
            - "improved_answer": string

            Output ONLY the raw JSON.
            """

            response = self._client.chat.completions.create(
                model=self._model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                response_format={"type": "json_object"},
            )

            content = response.choices[0].message.content
            if not content:
                raise InfrastructureError("Empty response from AI service")

            data = json.loads(content)

            return InterviewEvaluation(
                score=data.get("score", 5),
                strengths=data.get("strengths", []),
                weaknesses=data.get("weaknesses", []),
                improved_answer=data.get("improved_answer", ""),
            )

        except json.JSONDecodeError as e:
            raise InfrastructureError(
                "Invalid JSON response from AI service",
                details={"error": str(e)},
            )
        except Exception as e:
            raise InfrastructureError(
                "Failed to evaluate answer",
                details={"error": str(e)},
            )
