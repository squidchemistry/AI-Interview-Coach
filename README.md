# AI Interview Coach

Welcome to **AI Interview Coach**! This is a full-stack application that provides AI-powered interview practice. The application is designed as a **trial model** - no signup or authentication required.

---

## **Project Overview**

AI Interview Coach is a full-stack application with the following architecture:

- **Frontend**: Built with React, provides the user interface for interview practice.
- **Backend**: Powered by FastAPI, serves as the API gateway and handles interview logic.
- **AI Integration**: Uses Groq API (Llama 3.1 8B Instant) for generating questions and evaluating answers.
- **No Database**: Trial model - no user accounts or data persistence required.

---

## **Folder Structure**

### **Frontend**
Located in the `frontend/` folder:
- React components and UI
- API service layer for backend communication

### **Backend**
Located in the root `app/` folder following clean architecture:

- **`app/domain/interview/`**: Domain entities and business logic
- **`app/application/interview/`**: Use cases, DTOs, and interfaces
- **`app/infrastructure/ai/`**: Groq AI service implementation
- **`app/api/routes/interview.py`**: FastAPI routes for interview endpoints
- **`app/shared/`**: Cross-cutting utilities (errors, Result type)

### **Main Entry Point**
- **`main.py`**: FastAPI application factory and startup

---

## **How to Run the Project**

### **Option 1: Integrated Deployment (Recommended for Production)**

Deploy frontend and backend together in a single container:

1. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your GROQ_API_KEY
   ```

2. **Build and run with Docker**:
   ```bash
   docker-compose up --build
   ```

   The application will be available at `http://localhost:8000`
   - Frontend: `http://localhost:8000`
   - API docs: `http://localhost:8000/docs`
   - Health check: `http://localhost:8000/ping`

### **Option 2: Development Mode (Separate Frontend/Backend)**

Run frontend and backend separately for development:

#### **Backend Setup**

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set environment variable:
   ```bash
   # Create a .env file or export:
   export GROQ_API_KEY=your_groq_api_key_here
   ```

4. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`
   - API docs: `http://localhost:8000/docs`
   - Health check: `http://localhost:8000/ping`

#### **Frontend Setup**

1. Navigate to the `frontend/` folder:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create `.env` file (optional, defaults to `http://localhost:8000`):
   ```bash
   echo "REACT_APP_API_URL=http://localhost:8000" > .env
   ```

4. Start the development server:
   ```bash
   npm start
   ```

   The frontend will be available at `http://localhost:3000`

### **Prerequisites**
- Install **Python 3.9+**
- Install **Node.js** and **npm** (for frontend development)
- Install **Docker** and **Docker Compose** (for integrated deployment)
- Get a **Groq API key** from https://console.groq.com

---

## **API Endpoints**

### **Generate Interview Questions**
```http
POST /v1/interview/generate-questions
Content-Type: application/json

{
  "role": "Software Engineer",
  "experience": "2 years"
}
```

**Response:**
```json
{
  "questions": [
    "What is the difference between a list and a tuple in Python?",
    "Explain the concept of RESTful APIs.",
    ...
  ]
}
```

### **Evaluate Answer**
```http
POST /v1/interview/evaluate
Content-Type: application/json

{
  "question": "What is the difference between a list and a tuple?",
  "answer": "A list is mutable while a tuple is immutable..."
}
```

**Response:**
```json
{
  "score": 8,
  "strengths": ["Clear explanation", "Good examples"],
  "weaknesses": ["Could mention performance implications"],
  "improved_answer": "A list is mutable... [improved version]"
}
```

---

## **Architecture**

The backend follows **Clean Architecture** principles:

- **Domain Layer**: Pure business logic (entities, domain rules)
- **Application Layer**: Use cases that orchestrate domain logic
- **Infrastructure Layer**: External services (Groq API)
- **API Layer**: FastAPI routes and HTTP handling

This structure ensures:
- Business logic is independent of external services
- Easy to test and maintain
- Simple to add new features

---

## **Technology Stack**

- **Backend**: FastAPI, Python 3.9+
- **AI Service**: Groq API (Llama 3.1 8B Instant)
- **Frontend**: React
- **Validation**: Pydantic

---

## **Features**

✅ **No Signup Required** - Open trial model  
✅ **AI-Powered Questions** - Generate questions based on role and experience  
✅ **Answer Evaluation** - Get scores, strengths, weaknesses, and improved answers  
✅ **Clean Architecture** - Maintainable and scalable codebase  

---

## **Deployment**

For step-by-step deployment instructions, see [DEPLOYMENT_STEPS.md](./DEPLOYMENT_STEPS.md).

For detailed deployment guide, see [DEPLOYMENT.md](./DEPLOYMENT.md).

### **Quick Deploy**

```bash
# 1. Set environment variables
export GROQ_API_KEY=your_key_here

# 2. Build and run
docker-compose up --build

# 3. Access the app
open http://localhost:8000
```

### **Environment Variables**

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Groq API key for AI services | Yes |
| `CORS_ORIGINS` | Comma-separated allowed origins | No (has defaults) |
| `APP_ENV` | Environment (development/production) | No |
| `ENABLE_DOCS` | Enable API documentation | No (default: true) |

## **Contributing**

We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Submit a pull request with a detailed description of your changes

---

## **Contact**

If you have any questions, feel free to reach out to the project maintainers.

Happy coding!
