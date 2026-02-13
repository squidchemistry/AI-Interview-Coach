# Troubleshooting Guide

Common errors and their solutions for AI Interview Coach deployment.

---

## 🔴 Docker Build Errors

### Error: `npm ci --only=production` fails
**Solution**: Fixed in Dockerfile. The correct command is `npm ci` (without `--only=production` flag).

### Error: `package-lock.json` not found
**Solution**: 
```bash
cd frontend
npm install
# This will create package-lock.json
```

### Error: `Module not found` during Docker build
**Solution**: 
```bash
# Clean Docker cache and rebuild
docker system prune -a
docker-compose build --no-cache
```

---

## 🔴 Python/Backend Errors

### Error: `GROQ_API_KEY` not found
**Solution**: 
```bash
# Make sure .env file exists in project root
cat .env
# Should contain: GROQ_API_KEY=your_key_here

# Or export directly
export GROQ_API_KEY=your_key_here
```

### Error: `cors_origins` duplicate field
**Solution**: Fixed in `app/infrastructure/config/settings.py`. Remove duplicate `cors_origins` field definition.

### Error: `ModuleNotFoundError: No module named 'app'`
**Solution**: 
```bash
# Make sure you're running from project root
cd /path/to/AI-Interview-Coach
uvicorn main:app --reload
```

### Error: `pydantic.errors.ConfigError`
**Solution**: Check that all required fields in `.env` are set:
- `GROQ_API_KEY` (required)
- `CORS_ORIGINS` (optional, has default)

---

## 🔴 Frontend Errors

### Error: `Cannot GET /`
**Solution**: 
- Make sure frontend is built: `cd frontend && npm run build`
- Copy build to static: `cp -r frontend/build ./static`
- Or use Docker which handles this automatically

### Error: `Network Error` or CORS errors
**Solution**: 
1. Check CORS_ORIGINS in `.env` includes your frontend URL
2. Verify frontend API calls use `/v1` prefix
3. Check backend is running: `curl http://localhost:8000/ping`

### Error: `REACT_APP_API_URL` not working
**Solution**: 
- Create `frontend/.env` file:
  ```env
  REACT_APP_API_URL=http://localhost:8000
  ```
- Restart frontend dev server after changing `.env`

---

## 🔴 Runtime Errors

### Error: Port 8000 already in use
**Solution**: 
```bash
# Find process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac:
lsof -ti:8000 | xargs kill -9

# Or change port in docker-compose.yml
ports:
  - "8001:8000"  # Use port 8001 instead
```

### Error: `StaticFiles` mount conflicts with routes
**Solution**: Fixed in `main.py`. Static files are mounted last, after API routes.

### Error: Frontend shows blank page
**Solution**: 
1. Check browser console for errors
2. Verify static files exist: `ls static/` (should have index.html)
3. Check backend logs: `docker-compose logs app`
4. Verify API is working: `curl http://localhost:8000/ping`

---

## 🔴 Groq API Errors

### Error: `Invalid API key`
**Solution**: 
- Verify your Groq API key is correct
- Check key starts with `gsk_`
- Ensure no extra spaces in `.env` file
- Regenerate key at https://console.groq.com if needed

### Error: `Rate limit exceeded`
**Solution**: 
- Groq has rate limits on free tier
- Wait a few minutes and retry
- Consider upgrading plan if needed

### Error: `Model not found`
**Solution**: 
- Check `groq_service.py` uses correct model name
- Default: `llama-3.1-8b-instant`
- Verify model is available in your Groq account

---

## 🔴 Docker Compose Errors

### Error: `service "app" depends on undefined service "db"`
**Solution**: 
- Old docker-compose.yml had database service
- Current version doesn't need database
- Use updated `docker-compose.yml` from repository

### Error: `env_file .env not found`
**Solution**: 
```bash
# Create .env file
cp .env.example .env
# Edit and add your GROQ_API_KEY
```

### Error: `Cannot connect to Docker daemon`
**Solution**: 
- Make sure Docker Desktop is running
- Restart Docker Desktop
- Check: `docker ps` should work

---

## ✅ Quick Fixes

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

# Test backend directly
python -c "from app.infrastructure.config.settings import get_settings; print(get_settings().groq_api_key[:10])"
```

---

## 🆘 Still Having Issues?

1. **Check logs**: `docker-compose logs app`
2. **Verify environment**: Ensure `.env` file exists and has correct values
3. **Test components separately**:
   - Backend: `uvicorn main:app --reload`
   - Frontend: `cd frontend && npm start`
4. **Check versions**:
   - Python: `python --version` (should be 3.9+)
   - Node: `node --version` (should be 18+)
   - Docker: `docker --version`

---

## Common Error Messages Reference

| Error Message | Likely Cause | Solution |
|--------------|--------------|----------|
| `GROQ_API_KEY` not found | Missing env var | Add to `.env` file |
| Port 8000 in use | Another service running | Kill process or change port |
| Module not found | Wrong directory | Run from project root |
| CORS error | Frontend URL not in CORS_ORIGINS | Update `.env` CORS_ORIGINS |
| npm ci failed | Invalid npm command | Use `npm ci` (fixed in Dockerfile) |
| Static files not found | Frontend not built | Run `npm run build` in frontend |
