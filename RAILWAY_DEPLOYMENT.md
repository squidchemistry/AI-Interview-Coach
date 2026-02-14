# Railway Deployment Guide - AI Interview Coach

## ✅ Fixed: Frontend Submodule Issue

The frontend has been converted from a git submodule to a regular directory, so Railway can now build it successfully!

## 🚀 Deploy to Railway (Step-by-Step)

### Step 1: Go to Railway
1. Open your browser and go to: **https://railway.app**
2. Click **"Login"** or **"Start a New Project"**
3. Sign in with your GitHub account

### Step 2: Create New Project
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose **"squidchemistry/AI-Interview-Coach"**
4. Railway will automatically detect the Dockerfile

### Step 3: Add Environment Variable
1. Once the project is created, click on your service
2. Go to the **"Variables"** tab
3. Click **"+ New Variable"**
4. Add:
   - **Variable Name**: `GROQ_API_KEY`
   - **Value**: `gsk_nZEeXHm6Yz30udQNtzSbXCpRPb3FYHvqKNOX7yD0` (your key)
5. Click **"Add"**

### Step 4: Deploy
Railway will automatically:
- ✅ Detect the Dockerfile
- ✅ Build the React frontend (Node 20)
- ✅ Install Python dependencies
- ✅ Create a production container
- ✅ Deploy to a public URL

### Step 5: Get Your URL
1. Go to the **"Settings"** tab
2. Scroll to **"Domains"**
3. Click **"Generate Domain"**
4. Your app will be available at: `https://your-app.railway.app`

## 🎯 What Railway Will Do

Railway will execute your Dockerfile:
```dockerfile
# Stage 1: Build React frontend with Node 20
FROM node:20-alpine
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Python backend + frontend static files
FROM python:3.11-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ ./app/
COPY main.py .
COPY --from=frontend-builder /app/frontend/build ./static
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## ✅ Verify Deployment

Once deployed, test these URLs (replace with your Railway URL):

1. **Frontend**: `https://your-app.railway.app/`
2. **Health Check**: `https://your-app.railway.app/ping`
   - Should return: `{"status":"alive"}`
3. **API Docs**: `https://your-app.railway.app/docs`
4. **Generate Questions**: `POST https://your-app.railway.app/v1/interview/generate-questions`

## 🔧 Troubleshooting

### Build Still Failing?
1. Check Railway build logs for errors
2. Ensure `GROQ_API_KEY` is set in Variables tab
3. Try redeploying: Click "Deploy" → "Redeploy"

### App Not Responding?
1. Check the **"Deployments"** tab - ensure status is "Success"
2. Check **"Logs"** tab for runtime errors
3. Verify the domain is generated in Settings

### Need to Update Code?
Just push to GitHub:
```bash
git add .
git commit -m "Update code"
git push origin main
```
Railway will automatically redeploy!

## 💰 Pricing
- **Free Tier**: $5 credit per month (enough for development/testing)
- **Hobby Plan**: $5/month for more resources
- Your app will sleep after inactivity on free tier

## 🎉 Success!
Once deployed, your AI Interview Coach will be live at your Railway URL!

Share the link with anyone to try your interview coach! 🚀
