from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.interview.routes import router as interview_router

app = FastAPI(title="AI Interview Coach API")

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register interview module
app.include_router(interview_router, prefix="/interview")

@app.get("/ping")
def ping():
    return {"status": "alive"}
