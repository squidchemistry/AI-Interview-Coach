# Deployment Steps - AI Interview Coach

This guide provides step-by-step instructions for deploying the AI Interview Coach application.

---

## 📋 Prerequisites

Before starting, ensure you have:

- ✅ **Docker** and **Docker Compose** installed
  - Check: `docker --version` and `docker-compose --version`
  - Download: https://www.docker.com/get-started

- ✅ **Groq API Key**
  - Sign up at: https://console.groq.com
  - Get your API key from the dashboard

- ✅ **Git** (if cloning from repository)
  - Check: `git --version`

---

## 🚀 Quick Deployment (Docker - Recommended)

### Step 1: Clone/Download the Project

```bash
# If using Git
git clone <repository-url>
cd AI-Interview-Coach

# Or download and extract the project folder
```

### Step 2: Create Environment File

Create a `.env` file in the project root:

```bash
# Copy the example file
cp .env.example .env

# Or create manually
touch .env
```

Edit `.env` and add your configuration:

```env
# Required: Your Groq API Key
GROQ_API_KEY=gsk_your_actual_api_key_here

# Optional: CORS Origins (comma-separated)
CORS_ORIGINS=http://localhost:3000,http://localhost:5173,http://localhost:8000

# Optional: Application Settings
APP_ENV=production
APP_NAME=AI Interview Coach
APP_VERSION=0.1.0
ENABLE_DOCS=true
```

**⚠️ Important:** Replace `gsk_your_actual_api_key_here` with your actual Groq API key!

### Step 3: Build and Start the Application

```bash
# Build and start in one command
docker-compose up --build

# Or run in detached mode (background)
docker-compose up -d --build
```

### Step 4: Verify Deployment

Open your browser and check:

- **Main Application**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/ping

You should see:
- ✅ Frontend loads correctly
- ✅ API docs show available endpoints
- ✅ Health check returns `{"status": "alive"}`

### Step 5: Test the Application

1. Go to http://localhost:8000
2. Fill in:
   - **Role**: e.g., "Software Engineer"
   - **Experience**: e.g., "2 years"
3. Click "Generate Interview Questions"
4. Answer the questions
5. Review your evaluation

---

## 🔧 Manual Deployment (Without Docker)

### Step 1: Set Up Backend

```bash
# Navigate to project root
cd AI-Interview-Coach

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### Step 2: Set Up Frontend

```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Build the frontend for production
npm run build

# Go back to project root
cd ..
```

### Step 3: Copy Frontend Build

```bash
# Copy the built frontend to static directory
# On Windows:
xcopy /E /I frontend\build static
# On macOS/Linux:
cp -r frontend/build ./static
```

### Step 4: Configure Environment

Create `.env` file in project root:

```env
GROQ_API_KEY=your_groq_api_key_here
CORS_ORIGINS=http://localhost:8000
APP_ENV=production
```

### Step 5: Start the Backend Server

```bash
# Make sure you're in the project root
# Make sure virtual environment is activated

# Start the server
uvicorn main:app --host 0.0.0.0 --port 8000

# Or for production with multiple workers:
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Step 6: Access the Application

Open http://localhost:8000 in your browser.

---

## ☁️ Cloud Platform Deployment

### Option 1: Railway

1. **Create Railway Account**
   - Go to https://railway.app
   - Sign up/login

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo" (or upload code)

3. **Configure Environment Variables**
   - Go to "Variables" tab
   - Add: `GROQ_API_KEY=your_key_here`
   - Add: `CORS_ORIGINS=https://your-app.railway.app`

4. **Configure Build Settings**
   - Build Command: `pip install -r requirements.txt && cd frontend && npm install && npm run build`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

5. **Deploy**
   - Railway will automatically build and deploy
   - Get your app URL from the dashboard

### Option 2: Render

1. **Create Render Account**
   - Go to https://render.com
   - Sign up/login

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure Settings**
   - **Build Command**: 
     ```bash
     pip install -r requirements.txt && cd frontend && npm install && npm run build
     ```
   - **Start Command**: 
     ```bash
     uvicorn main:app --host 0.0.0.0 --port $PORT
     ```
   - **Environment**: Python 3

4. **Add Environment Variables**
   - `GROQ_API_KEY`: your Groq API key
   - `CORS_ORIGINS`: your Render app URL

5. **Deploy**
   - Click "Create Web Service"
   - Render will build and deploy automatically

### Option 3: Heroku

1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Create Procfile**
   ```bash
   echo "web: uvicorn main:app --host 0.0.0.0 --port \$PORT" > Procfile
   ```

3. **Login and Create App**
   ```bash
   heroku login
   heroku create your-app-name
   ```

4. **Set Environment Variables**
   ```bash
   heroku config:set GROQ_API_KEY=your_key_here
   heroku config:set CORS_ORIGINS=https://your-app-name.herokuapp.com
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

---

## 🔍 Troubleshooting

### Issue: "GROQ_API_KEY not found"
**Solution**: Make sure `.env` file exists and contains `GROQ_API_KEY=your_key`

### Issue: Frontend not loading
**Solution**: 
- Check that `static/` directory exists with frontend build files
- Verify Docker build completed successfully
- Check backend logs: `docker-compose logs app`

### Issue: CORS errors
**Solution**: 
- Add your frontend URL to `CORS_ORIGINS` in `.env`
- Restart the application

### Issue: Port 8000 already in use
**Solution**: 
- Change port in `docker-compose.yml`: `"8001:8000"`
- Or stop the service using port 8000

### Issue: Docker build fails
**Solution**:
```bash
# Clean Docker cache
docker system prune -a

# Rebuild without cache
docker-compose build --no-cache
```

### Issue: Frontend API calls failing
**Solution**:
- Verify API endpoints use `/v1` prefix
- Check browser console for errors
- Verify backend is running: `curl http://localhost:8000/ping`

---

## 📊 Monitoring & Health Checks

### Check Application Status

```bash
# Health check endpoint
curl http://localhost:8000/ping

# Expected response:
# {"status": "alive"}
```

### View Logs

```bash
# Docker logs
docker-compose logs -f app

# Or for specific service
docker-compose logs app
```

### Stop the Application

```bash
# Stop Docker containers
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

---

## 🔐 Security Checklist

Before deploying to production:

- [ ] Change default CORS origins to your production domain
- [ ] Use environment variables for all secrets (never commit `.env`)
- [ ] Enable HTTPS/SSL for production
- [ ] Set `APP_ENV=production`
- [ ] Consider disabling docs in production: `ENABLE_DOCS=false`
- [ ] Review and limit CORS origins to trusted domains only
- [ ] Use a reverse proxy (nginx) for production deployments

---

## 📝 Environment Variables Reference

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `GROQ_API_KEY` | ✅ Yes | Groq API key | `gsk_abc123...` |
| `CORS_ORIGINS` | No | Allowed origins (comma-separated) | `http://localhost:3000,https://myapp.com` |
| `APP_ENV` | No | Environment | `production` |
| `APP_NAME` | No | Application name | `AI Interview Coach` |
| `APP_VERSION` | No | Version | `0.1.0` |
| `ENABLE_DOCS` | No | Enable API docs | `true` or `false` |

---

## ✅ Deployment Checklist

- [ ] Prerequisites installed (Docker, Groq API key)
- [ ] `.env` file created with `GROQ_API_KEY`
- [ ] Application builds successfully
- [ ] Application starts without errors
- [ ] Frontend loads at http://localhost:8000
- [ ] API docs accessible at http://localhost:8000/docs
- [ ] Health check returns success
- [ ] Can generate interview questions
- [ ] Can evaluate answers
- [ ] CORS configured correctly (if needed)

---

## 🎉 Success!

If all steps completed successfully, your AI Interview Coach application is now deployed and ready to use!

**Next Steps:**
- Test all features
- Monitor logs for any issues
- Set up production domain (if deploying publicly)
- Configure SSL/HTTPS for production

---

## 📞 Need Help?

- Check logs: `docker-compose logs app`
- Review API docs: http://localhost:8000/docs
- Check health: http://localhost:8000/ping
