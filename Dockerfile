# Multi-stage build for integrated frontend + backend deployment

# Stage 1: Build frontend
FROM node:20-alpine AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Python backend with frontend static files
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY app/ ./app/
COPY main.py .

# Copy built frontend from builder stage
COPY --from=frontend-builder /app/frontend/build ./static

# Install a simple HTTP server to serve static files (or use FastAPI static files)
RUN pip install aiofiles

ENV APP_ENV=production
ENV APP_NAME="AI Interview Coach"
ENV APP_VERSION=0.1.0

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
