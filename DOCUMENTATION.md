# 📚 AI Interview Coach - Complete Documentation

> Comprehensive guide for deployment, implementation, and troubleshooting

---

## 📖 Table of Contents

1. [Deployment Guide](#-deployment-guide)
2. [Implementation Plan](#-implementation-plan)
3. [Troubleshooting](#-troubleshooting)
4. [Environment Variables](#-environment-variables)
5. [Architecture](#-architecture)

---

# 🚀 Deployment Guide

## Railway Deployment (Recommended)

### Prerequisites
- ✅ GitHub account
- ✅ Railway account (free tier available)
- ✅ Groq API key ([Get one here](https://console.groq.com))

### Quick Deploy Steps

#### 1. Prepare Your Repository
```bash
# Clone the repository
git clone https://github.com/squidchemistry/interviewcoach.git
cd interviewcoach

# Ensure all files are committed
git status
```

#### 2. Deploy to Railway

1. **Open Railway**
   - Go to https://railway.app
   - Sign in with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `squidchemistry/interviewcoach`

3. **Add Environment Variables**
   - Click on your service
   - Go to "Variables" tab
   - Add: `GROQ_API_KEY` = `your_groq_api_key_here`

4. **Generate Domain**
   - Go to "Settings" tab
   - Scroll to "Networking" section
   - Click "Generate Domain"
   - Copy your Railway URL

5. **Wait for Deployment**
   - Go to "Deployments" tab
   - Wait for build to complete (~3-5 minutes)
   - Status should show "Success" ✅

#### 3. Test Your Deployment

Visit these URLs (replace with your Railway URL):

```
https://your-app.railway.app/ping          # Health check
https://your-app.railway.app/docs          # API documentation
https://your-app.railway.app/              # Frontend application
```

### Custom Domain Setup

If you have a custom domain (e.g., `.tech` domain):

1. **In Railway:**
   - Settings → Networking → Custom Domain
   - Enter your domain: `yourdomain.tech`

2. **In Your Domain Registrar:**
   - Add CNAME record:
     - Type: `CNAME`
     - Name: `@` or `app`
     - Value: `your-app.up.railway.app`
     - TTL: `3600`

3. **Wait for DNS Propagation** (10-30 minutes)

4. **SSL Certificate**
   - Railway automatically provisions SSL
   - Your site will be accessible via HTTPS

---

## Docker Deployment (Local)

### Build and Run

```bash
# 1. Set environment variables
cp .env.example .env
# Edit .env and add your GROQ_API_KEY

# 2. Build and run with Docker
docker-compose up --build

# 3. Access the application
# Frontend: http://localhost:8000
# API Docs: http://localhost:8000/docs
# Health: http://localhost:8000/ping
```

### Docker Commands

```bash
# Stop containers
docker-compose down

# View logs
docker-compose logs -f

# Rebuild without cache
docker-compose build --no-cache

# Remove volumes
docker-compose down -v
```

---

## Development Mode (Local)

### Backend Setup

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set environment variable
export GROQ_API_KEY=your_key_here  # Windows: set GROQ_API_KEY=your_key_here

# 4. Run server
uvicorn main:app --reload
```

Backend will be available at: http://localhost:8000

### Frontend Setup

```bash
# 1. Navigate to frontend
cd frontend

# 2. Install dependencies
npm install

# 3. Create .env file (optional)
echo "REACT_APP_API_URL=http://localhost:8000" > .env

# 4. Start development server
npm start
```

Frontend will be available at: http://localhost:3000

---

# 📋 Implementation Plan

## Upcoming Features

### Phase 1: User Authentication & Database

#### Database Schema (CockroachDB)

**Users Table:**
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255),
    google_id VARCHAR(255) UNIQUE,
    name VARCHAR(255) NOT NULL,
    profile_picture VARCHAR(500),
    role VARCHAR(20) DEFAULT 'user',  -- 'user' or 'admin'
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now(),
    last_login TIMESTAMP
);
```

**User Profiles Table:**
```sql
CREATE TABLE user_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE UNIQUE,
    bio TEXT,
    github_url VARCHAR(255),
    linkedin_url VARCHAR(255),
    twitter_url VARCHAR(255),
    portfolio_url VARCHAR(255),
    location VARCHAR(255),
    current_role VARCHAR(255),
    experience_level VARCHAR(50),
    updated_at TIMESTAMP DEFAULT now()
);
```

**Interview Sessions Table:**
```sql
CREATE TABLE interview_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    role VARCHAR(255),
    experience VARCHAR(50),
    questions JSONB,
    answers JSONB,
    scores JSONB,
    duration_seconds INT,
    created_at TIMESTAMP DEFAULT now(),
    completed_at TIMESTAMP
);
```

**User Streaks Table:**
```sql
CREATE TABLE user_streaks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE UNIQUE,
    current_streak INT DEFAULT 0,
    longest_streak INT DEFAULT 0,
    last_practice_date DATE,
    total_sessions INT DEFAULT 0,
    total_questions_answered INT DEFAULT 0,
    updated_at TIMESTAMP DEFAULT now()
);
```

**Analytics Events Table:**
```sql
CREATE TABLE analytics_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_type VARCHAR(50),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    ip_address VARCHAR(45),
    user_agent TEXT,
    path VARCHAR(500),
    method VARCHAR(10),
    status_code INT,
    response_time_ms INT,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT now()
);
```

**System Settings Table:**
```sql
CREATE TABLE system_settings (
    key VARCHAR(100) PRIMARY KEY,
    value TEXT,
    description TEXT,
    updated_at TIMESTAMP DEFAULT now(),
    updated_by UUID REFERENCES users(id)
);
```

#### Authentication System

**Backend Components:**
- Password hashing (bcrypt)
- JWT token management
- Google OAuth integration
- User registration/login endpoints
- Protected route middleware

**Frontend Components:**
- Login/Signup pages
- Google Sign-In button
- Auth context provider
- Protected routes
- Token management

#### API Endpoints

**Authentication:**
```
POST /v1/auth/register
POST /v1/auth/login
POST /v1/auth/google/url
POST /v1/auth/google/callback
POST /v1/auth/refresh
GET /v1/auth/me
```

**User Profile:**
```
GET /v1/users/me
PUT /v1/users/me
GET /v1/users/me/profile
PUT /v1/users/me/profile
GET /v1/users/me/streak
```

---

### Phase 2: Streak Tracking System

#### Streak Logic

```python
def update_streak(user_id):
    today = date.today()
    streak = get_user_streak(user_id)
    
    if streak.last_practice_date == today:
        # Already practiced today
        return streak
    
    if streak.last_practice_date == today - timedelta(days=1):
        # Consecutive day - increment streak
        streak.current_streak += 1
        streak.longest_streak = max(streak.current_streak, streak.longest_streak)
    else:
        # Streak broken - reset
        streak.current_streak = 1
    
    streak.last_practice_date = today
    streak.total_sessions += 1
    save_streak(streak)
    return streak
```

#### UI Components

- Streak widget with flame icon 🔥
- Calendar view of practice days
- Motivational messages
- Longest streak badge
- Total sessions count

---

### Phase 3: Admin Dashboard

#### Admin Features

**Overview Stats:**
- Total users
- Active users (last 7/30 days)
- Total interview sessions
- Sessions today/week/month
- Average session duration
- Most popular interview roles

**User Management:**
- View all users
- Search/filter users
- Activate/deactivate accounts
- View user details and activity

**Analytics:**
- Traffic charts (requests per hour/day)
- API endpoint usage
- Response time trends
- Error rate tracking
- Geographic distribution

**System Control:**
- Maintenance mode toggle
- Custom maintenance message
- System settings management

#### Admin Endpoints

```
GET /v1/admin/stats/overview
GET /v1/admin/stats/users
GET /v1/admin/stats/sessions
GET /v1/admin/stats/traffic
GET /v1/admin/users
GET /v1/admin/users/{user_id}
PUT /v1/admin/users/{user_id}/status
POST /v1/admin/maintenance/enable
POST /v1/admin/maintenance/disable
GET /v1/admin/analytics/events
```

---

### Phase 4: User Profiles

#### Profile Features

- Personal information (name, bio, location)
- Social links (GitHub, LinkedIn, Twitter, Portfolio)
- Current role and experience level
- Profile picture
- Interview history
- Streak statistics

#### Profile UI

- Profile view page
- Edit profile form
- Social links section
- Statistics dashboard
- Interview history timeline

---

## Implementation Timeline

### Week 1: Database & Auth
- Day 1-2: Set up CockroachDB, create schema
- Day 3-4: Implement authentication (JWT + Google OAuth)
- Day 5: Create login/signup UI

### Week 2: Profiles & Streaks
- Day 6-7: User profiles and social links
- Day 8-9: Streak tracking system
- Day 10: Streak UI components

### Week 3: Admin Dashboard
- Day 11-12: Admin backend (analytics, user management)
- Day 13-14: Admin UI (dashboard, charts)
- Day 15: Maintenance mode and system settings

### Week 4: Testing & Polish
- Day 16-17: Integration testing
- Day 18-19: Bug fixes and UI polish
- Day 20: Production deployment

---

# 🔧 Troubleshooting

## Common Issues

### Docker Build Errors

**Error: `npm ci --only=production` fails**
```bash
# Solution: Use npm install instead
# Already fixed in Dockerfile
```

**Error: `package-lock.json` not found**
```bash
cd frontend
npm install  # This creates package-lock.json
```

**Error: Module not found during build**
```bash
# Clean Docker cache and rebuild
docker system prune -a
docker-compose build --no-cache
```

---

### Backend Errors

**Error: `GROQ_API_KEY` not found**
```bash
# Create .env file
cp .env.example .env

# Add your key
echo "GROQ_API_KEY=your_key_here" >> .env

# Or export directly
export GROQ_API_KEY=your_key_here
```

**Error: `ModuleNotFoundError: No module named 'app'`**
```bash
# Make sure you're in project root
cd /path/to/AI-Interview-Coach
uvicorn main:app --reload
```

**Error: Port 8000 already in use**
```bash
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac:
lsof -ti:8000 | xargs kill -9
```

---

### Frontend Errors

**Error: `Cannot GET /`**
```bash
# Build frontend
cd frontend && npm run build

# Or use Docker which handles this automatically
docker-compose up --build
```

**Error: Network Error or CORS errors**
```bash
# Check CORS_ORIGINS in .env
CORS_ORIGINS=http://localhost:3000,https://passmeai.tech

# Verify backend is running
curl http://localhost:8000/ping
```

**Error: Frontend shows blank page**
1. Check browser console for errors
2. Verify static files exist: `ls static/`
3. Check backend logs: `docker-compose logs app`
4. Test API: `curl http://localhost:8000/ping`

---

### Groq API Errors

**Error: `Invalid API key`**
- Verify key is correct
- Check key starts with `gsk_`
- Ensure no extra spaces in .env
- Regenerate key at https://console.groq.com

**Error: `Rate limit exceeded`**
- Groq has rate limits on free tier
- Wait a few minutes and retry
- Consider upgrading plan if needed

---

### Railway Deployment Errors

**Error: Build fails with "package.json not found"**
```bash
# Ensure latest commit is deployed
# Railway → Deployments → Redeploy
# Check it's pulling from main branch
```

**Error: "GROQ_API_KEY not found" in Railway**
```bash
# Add environment variable in Railway
# Variables tab → Add Variable
# Name: GROQ_API_KEY
# Value: your_key_here
```

**Error: App not responding**
1. Check Deployments tab - ensure status is "Success"
2. Check Logs tab for runtime errors
3. Verify domain is generated in Settings
4. Test health endpoint: `/ping`

---

## Quick Fixes

### Reset Everything
```bash
# Stop containers
docker-compose down

# Remove volumes
docker-compose down -v

# Clean build
docker-compose build --no-cache

# Start fresh
docker-compose up
```

### Check Logs
```bash
# All services
docker-compose logs

# Specific service
docker-compose logs app

# Follow logs
docker-compose logs -f app
```

### Verify Environment
```bash
# Check .env file
cat .env

# Test backend
python -c "from app.infrastructure.config.settings import get_settings; print(get_settings().groq_api_key[:10])"
```

---

# 🔑 Environment Variables

## Backend (.env)

```env
# Required
GROQ_API_KEY=your_groq_api_key_here

# Optional (with defaults)
APP_ENV=production
CORS_ORIGINS=http://localhost:3000,https://passmeai.tech
ENABLE_DOCS=true

# Future (for authentication)
DATABASE_URL=postgresql://user:pass@cluster.cockroachlabs.cloud:26257/defaultdb
JWT_SECRET_KEY=your-super-secret-key-here
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=https://passmeai.tech/v1/auth/google/callback
ADMIN_EMAIL=your-email@example.com
```

## Frontend (.env)

```env
# API URL (defaults to window.location.origin in production)
REACT_APP_API_URL=http://localhost:8000

# Future (for Google OAuth)
REACT_APP_GOOGLE_CLIENT_ID=your-google-client-id
```

---

# 🏗️ Architecture

## Clean Architecture Layers

### Domain Layer
- **Entities**: Core business objects (User, InterviewQuestion, InterviewEvaluation)
- **Business Rules**: Domain logic and validation
- **Exceptions**: Domain-specific errors

### Application Layer
- **Use Cases**: Orchestrate domain logic (RegisterUser, GenerateQuestions, EvaluateAnswer)
- **DTOs**: Data Transfer Objects for API requests/responses
- **Interfaces**: Abstract contracts (UserRepository, AIService)

### Infrastructure Layer
- **Database**: SQLAlchemy models and repositories
- **External Services**: Groq AI service, Google OAuth
- **Configuration**: Settings and environment management

### API Layer
- **Routes**: FastAPI endpoints
- **Middleware**: CORS, analytics tracking, maintenance mode
- **Error Handlers**: Centralized error handling

## Technology Stack

**Backend:**
- FastAPI (web framework)
- Python 3.11
- Pydantic (validation)
- SQLAlchemy (ORM - future)
- Groq API (AI service)

**Frontend:**
- React 18
- React Router
- Axios (HTTP client)

**Database (Future):**
- CockroachDB (distributed SQL)

**DevOps:**
- Docker & Docker Compose
- Railway (deployment)
- GitHub (version control)

---

## Project Structure

```
AI-Interview-Coach/
├── app/
│   ├── api/
│   │   ├── routes/          # API endpoints
│   │   └── middleware/      # Request/response middleware
│   ├── application/
│   │   ├── interview/       # Interview use cases
│   │   ├── users/           # User use cases (future)
│   │   └── admin/           # Admin use cases (future)
│   ├── domain/
│   │   ├── interview/       # Interview entities
│   │   ├── users/           # User entities (future)
│   │   └── streaks/         # Streak entities (future)
│   ├── infrastructure/
│   │   ├── ai/              # Groq AI service
│   │   ├── auth/            # Authentication (future)
│   │   ├── config/          # Settings
│   │   └── db/              # Database (future)
│   └── shared/
│       ├── errors.py        # Error definitions
│       └── result.py        # Result pattern
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/      # React components
│       ├── pages/           # Page components
│       ├── services/        # API service
│       └── contexts/        # React contexts (future)
├── main.py                  # FastAPI application
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose setup
├── requirements.txt         # Python dependencies
└── README.md                # Project overview
```

---

## API Documentation

### Current Endpoints

**Health Check:**
```http
GET /ping
Response: {"status": "alive"}
```

**Generate Questions:**
```http
POST /v1/interview/generate-questions
Content-Type: application/json

{
  "role": "Software Engineer",
  "experience": "2 years"
}

Response:
{
  "questions": [
    "What is the difference between a list and a tuple in Python?",
    "Explain the concept of RESTful APIs.",
    ...
  ]
}
```

**Evaluate Answer:**
```http
POST /v1/interview/evaluate
Content-Type: application/json

{
  "question": "What is the difference between a list and a tuple?",
  "answer": "A list is mutable while a tuple is immutable..."
}

Response:
{
  "score": 8,
  "strengths": ["Clear explanation", "Good examples"],
  "weaknesses": ["Could mention performance implications"],
  "improved_answer": "A list is mutable... [improved version]"
}
```

---

## Security Considerations

### Current
- CORS protection
- Environment variable management
- API key security

### Future
- Password hashing (bcrypt)
- JWT token authentication
- Role-based access control (admin/user)
- Rate limiting
- HTTPS enforcement
- CSRF protection
- Input validation and sanitization

---

## Performance Optimization

### Current
- Static file serving
- Docker multi-stage builds
- Production-optimized frontend build

### Future
- Database query optimization
- Response caching
- CDN for static assets
- Load balancing
- Database connection pooling

---

## Monitoring & Analytics

### Current
- Railway built-in metrics
- Application logs

### Future
- Custom analytics dashboard
- User behavior tracking
- Error tracking and reporting
- Performance monitoring
- Uptime monitoring

---

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## License

MIT License - see LICENSE file for details

---

## Support

For issues or questions:
- GitHub Issues: https://github.com/squidchemistry/interviewcoach/issues
- Email: Contact repository owner

---

**Made with ❤️ by Arshv**

Live at: https://passmeai.tech
