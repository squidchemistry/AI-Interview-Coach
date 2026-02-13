from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class QuestionRequest(BaseModel):
    role: str
    experience: str

class EvaluationRequest(BaseModel):
    question: str
    answer: str

@router.post("/generate-questions")
def generate_questions_route(request: QuestionRequest):
    from .services import generate_questions
    questions = generate_questions(request.role, request.experience)
    return {"questions": questions}

@router.post("/evaluate")
def evaluate(request: EvaluationRequest):
    from .services import evaluate_answer
    return evaluate_answer(request.question, request.answer)
