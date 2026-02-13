# Vercel Deployment Guide

## ⚠️ Important Notes

**Vercel Limitations:**
- Vercel serverless functions have a 10-second execution timeout
- The frontend will be served as static files from the `static/` directory
- You need to build the frontend locally before deploying

## 📋 Steps to Deploy on Vercel

### 1. Build the Frontend Locally

```bash
cd frontend
npm install
npm run build
cd ..

# Copy build to static directory
# On Windows:
xcopy /E /I frontend\build static

# On macOS/Linux:
cp -r frontend/build ./static
```

### 2. Deploy to Vercel

#### Option A: Using Vercel CLI
```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
vercel

# Set environment variable
vercel env add GROQ_API_KEY
# Paste your Groq API key when prompted
```

#### Option B: Using Vercel Dashboard
1. Go to https://vercel.com
2. Click "Add New" → "Project"
3. Import your GitHub repository
4. Add environment variable:
   - Name: `GROQ_API_KEY`
   - Value: Your Groq API key
5. Click "Deploy"

### 3. Verify Deployment

Once deployed, test these endpoints:
- `https://your-app.vercel.app/ping` - Should return `{"status":"alive"}`
- `https://your-app.vercel.app/docs` - API documentation
- `https://your-app.vercel.app/` - Frontend application

## 🚀 Better Alternative: Railway or Render

**Vercel is NOT ideal for this project** because:
- It doesn't support Docker
- Serverless functions have timeout limits
- You need to manually build the frontend

**Recommended: Use Railway or Render instead**

### Railway (Easiest):
1. Go to https://railway.app
2. "New Project" → "Deploy from GitHub"
3. Select your repo
4. Add `GROQ_API_KEY` environment variable
5. Railway auto-detects Dockerfile and deploys everything

### Render:
1. Go to https://render.com
2. "New Web Service"
3. Connect GitHub repo
4. Add `GROQ_API_KEY` environment variable
5. Render auto-deploys with Docker

Both Railway and Render will:
- ✅ Build frontend automatically
- ✅ Run backend with no timeout limits
- ✅ Support Docker deployment
- ✅ Provide free tier

## 🔧 Troubleshooting Vercel

If you still get `{"detail":"Not Found"}`:

1. **Check the static directory exists:**
   ```bash
   ls static/
   # Should show: index.html, static/, etc.
   ```

2. **Verify environment variable:**
   - Go to Vercel dashboard → Settings → Environment Variables
   - Ensure `GROQ_API_KEY` is set

3. **Check deployment logs:**
   - Vercel dashboard → Deployments → Click on latest deployment
   - Check build and runtime logs

4. **Test API directly:**
   ```bash
   curl https://your-app.vercel.app/ping
   curl https://your-app.vercel.app/v1/interview/generate-questions
   ```
