import os
import json
from groq import Groq
from fastapi import HTTPException

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_questions(role: str, experience: str) -> list[str]:
    try:
        prompt = f"""
        Generate 5 realistic technical interview questions 
        for a {role} with {experience} of experience.
        Return a JSON object with a key "questions" containing a list of strings.
        Output ONLY the raw JSON.
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content
        data = json.loads(content)
        return data.get("questions", [])

    except Exception as e:
        print(f"Error generating questions: {e}")
        raise HTTPException(status_code=500, detail=str(e))


def evaluate_answer(question: str, answer: str) -> dict:
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

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content
        return json.loads(content)

    except Exception as e:
        print(f"Error evaluating answer: {e}")
        raise HTTPException(status_code=500, detail=str(e))
