# 🎯 AI Interview Coach

> AI-powered interview preparation platform to help you ace your next technical interview

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://your-app.railway.app)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![React](https://img.shields.io/badge/react-18.0+-61dafb.svg)](https://reactjs.org/)

---

## ✨ Features

- 🤖 **AI-Powered Questions** - Generate customized interview questions based on role and experience
- 📊 **Smart Evaluation** - Get detailed feedback with scores, strengths, and improvement suggestions
- 🔥 **Streak Tracking** - Stay motivated with daily practice streaks *(Coming Soon)*
- 👤 **User Profiles** - Track your progress and showcase your achievements *(Coming Soon)*
- 🔐 **Secure Authentication** - Google OAuth and email/password login *(Coming Soon)*
- 📈 **Admin Dashboard** - Monitor usage, analytics, and system health *(Coming Soon)*

---

## 🚀 Live Demo

**Try it now:** [https://passmeai.tech](https://passmeai.tech)

---

## 🛠️ Tech Stack

### **Backend**
- **FastAPI** - Modern, fast web framework for building APIs
- **Python 3.11** - Core programming language
- **Groq API** - AI-powered question generation and evaluation (Llama 3.1)
- **CockroachDB** - Distributed SQL database *(Coming Soon)*
- **SQLAlchemy** - ORM for database operations

### **Frontend**
- **React 18** - UI library
- **React Router** - Client-side routing
- **Axios** - HTTP client for API calls

### **DevOps**
- **Docker** - Containerization
- **Railway** - Cloud deployment platform
- **GitHub Actions** - CI/CD *(Coming Soon)*

---

## 📦 Quick Start

### **Prerequisites**
- Python 3.11+
- Node.js 20+
- Docker (optional, for containerized deployment)
- Groq API Key ([Get one here](https://console.groq.com))

### **1. Clone the Repository**
```bash
git clone https://github.com/squidchemistry/interviewcoach.git
cd interviewcoach
```

### **2. Set Up Environment Variables**
```bash
# Create .env file
cp .env.example .env

# Add your Groq API key
echo "GROQ_API_KEY=your_groq_api_key_here" >> .env
```

### **3. Run with Docker (Recommended)**
```bash
docker-compose up --build
```

The app will be available at:
- **Frontend:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/ping

### **4. Or Run Locally**

**Backend:**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

---

## 📖 API Documentation

### **Generate Questions**
```http
POST /v1/interview/generate-questions
Content-Type: application/json

{
  "role": "Software Engineer",
  "experience": "2 years"
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

**Full API documentation available at:** `/docs` when running the server

---

## 🏗️ Project Structure

```
AI-Interview-Coach/
├── app/                      # Backend application
│   ├── api/                  # API routes and endpoints
│   ├── application/          # Use cases and business logic
│   ├── domain/               # Domain entities and rules
│   ├── infrastructure/       # External services (AI, DB)
│   └── shared/               # Shared utilities
├── frontend/                 # React frontend
│   ├── public/               # Static assets
│   └── src/                  # React components
├── main.py                   # FastAPI application entry point
├── Dockerfile                # Docker configuration
├── docker-compose.yml        # Docker Compose setup
└── requirements.txt          # Python dependencies
```

---

## 🌟 Upcoming Features

- [ ] User authentication (Google OAuth + Email/Password)
- [ ] User profiles with social links (GitHub, LinkedIn)
- [ ] Daily practice streak tracking
- [ ] Interview history and progress tracking
- [ ] Admin dashboard with analytics
- [ ] Maintenance mode
- [ ] Performance metrics and monitoring

---

## 📊 Architecture

Built with **Clean Architecture** principles:

- **Domain Layer** - Core business logic and entities
- **Application Layer** - Use cases and orchestration
- **Infrastructure Layer** - External services (AI, Database)
- **API Layer** - HTTP endpoints and request handling

This ensures:
- ✅ Testable and maintainable code
- ✅ Independent of frameworks and external services
- ✅ Easy to extend with new features

---

## 🚀 Deployment

### **Deploy to Railway**

1. Fork this repository
2. Create a new project on [Railway](https://railway.app)
3. Connect your GitHub repository
4. Add environment variable: `GROQ_API_KEY`
5. Deploy! 🎉

**Detailed deployment guide:** [DEPLOY_TO_RAILWAY.md](./DEPLOY_TO_RAILWAY.md)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Arshv**

- GitHub: [@squidchemistry](https://github.com/squidchemistry)
- Project Link: [https://github.com/squidchemistry/interviewcoach](https://github.com/squidchemistry/interviewcoach)

---

## 🙏 Acknowledgments

- [Groq](https://groq.com) for providing the AI API
- [FastAPI](https://fastapi.tiangolo.com/) for the amazing web framework
- [Railway](https://railway.app) for seamless deployment
- [CockroachDB](https://cockroachlabs.com) for the distributed database

---

## 📧 Contact

Have questions or suggestions? Feel free to open an issue or reach out!

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by Arshv

</div>
