# Deployment Guide

This guide covers deploying the AI Interview Coach application with integrated frontend and backend.

**📖 For detailed step-by-step instructions, see [DEPLOYMENT_STEPS.md](./DEPLOYMENT_STEPS.md)**

> **📋 For step-by-step instructions, see [DEPLOYMENT_STEPS.md](./DEPLOYMENT_STEPS.md)**

## Architecture

The application uses a unified deployment approach:
- **Backend**: FastAPI serves both API endpoints and static frontend files
- **Frontend**: React app is built and served as static files by FastAPI
- **Single Port**: Everything runs on port 8000

## Prerequisites

- Docker and Docker Compose installed
- Groq API key from https://console.groq.com

## Quick Start

### 1. Environment Setup

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
CORS_ORIGINS=http://localhost:3000,http://localhost:5173,http://localhost:8000
APP_ENV=production
```

### 2. Build and Run with Docker

```bash
# Build and start the application
docker-compose up --build

# Or run in detached mode
docker-compose up -d --build
```

The application will be available at:
- **Main App**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/ping

### 3. Development Mode (Separate Frontend/Backend)

For development, you can run frontend and backend separately:

#### Backend:
```bash
# Set environment variable
export GROQ_API_KEY=your_key_here

# Run backend
uvicorn main:app --reload
```

#### Frontend:
```bash
cd frontend

# Create .env file
echo "REACT_APP_API_URL=http://localhost:8000" > .env

# Install and run
npm install
npm start
```

## Production Deployment

### Option 1: Docker (Recommended)

The included `Dockerfile` uses multi-stage builds:
1. Builds the React frontend
2. Copies frontend build to Python container
3. Serves everything via FastAPI

```bash
docker build -t ai-interview-coach .
docker run -p 8000:8000 -e GROQ_API_KEY=your_key ai-interview-coach
```

### Option 2: Manual Deployment

1. **Build Frontend**:
   ```bash
   cd frontend
   npm install
   npm run build
   ```

2. **Copy Build to Backend**:
   ```bash
   cp -r frontend/build ./static
   ```

3. **Run Backend**:
   ```bash
   export GROQ_API_KEY=your_key
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

### Option 3: Cloud Platform Deployment

#### Heroku:
```bash
# Create Procfile
echo "web: uvicorn main:app --host 0.0.0.0 --port \$PORT" > Procfile

# Deploy
git push heroku main
```

#### Railway/Render:
- Connect your repository
- Set `GROQ_API_KEY` environment variable
- Build command: `pip install -r requirements.txt && cd frontend && npm install && npm run build`
- Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GROQ_API_KEY` | **Required** - Groq API key | - |
| `CORS_ORIGINS` | Comma-separated list of allowed origins | `http://localhost:3000,http://localhost:5173` |
| `APP_ENV` | Environment (development/production) | `development` |
| `ENABLE_DOCS` | Enable API documentation | `true` |
| `APP_NAME` | Application name | `AI Interview Coach` |

## API Endpoints

All API endpoints are prefixed with `/v1`:

- `POST /v1/interview/generate-questions` - Generate interview questions
- `POST /v1/interview/evaluate` - Evaluate an answer
- `GET /ping` - Health check
- `GET /docs` - API documentation (Swagger UI)

## Frontend Configuration

The frontend automatically detects the API URL:
- **Development**: Uses `REACT_APP_API_URL` from `.env` or defaults to `http://localhost:8000`
- **Production**: Uses the same origin (relative URLs work when served by FastAPI)

## Troubleshooting

### CORS Errors
- Ensure `CORS_ORIGINS` includes your frontend URL
- Check that the frontend is calling the correct API URL

### Frontend Not Loading
- Verify the `static/` directory exists with built frontend files
- Check that FastAPI is serving static files correctly

### API Errors
- Verify `GROQ_API_KEY` is set correctly
- Check backend logs for detailed error messages
- Ensure API endpoints use `/v1` prefix

## Monitoring

Health check endpoint:
```bash
curl http://localhost:8000/ping
```

Expected response:
```json
{"status": "alive"}
```
