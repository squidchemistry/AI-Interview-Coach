# Railway Deployment

This project is configured for Railway deployment using Docker.

## Quick Deploy

1. Go to https://railway.app
2. New Project → Deploy from GitHub repo
3. Select this repository
4. Add environment variable: `GROQ_API_KEY`
5. Railway will automatically build using the Dockerfile

## What Gets Built

- Frontend: React app (Node 20)
- Backend: FastAPI (Python 3.11)
- All served from a single container on port 8000

## Environment Variables Required

- `GROQ_API_KEY` - Your Groq API key for AI functionality

## Deployment Status

✅ Frontend files are now properly included in the repository
✅ Dockerfile is configured for multi-stage build
✅ Ready for deployment!
