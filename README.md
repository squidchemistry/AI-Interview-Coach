# Project Alpha

Welcome to **Project Alpha**! This document provides a detailed overview of the project structure, its components, and how everything works together. This guide is designed to help newcomers quickly understand the project.

---

## **Project Overview**

Project Alpha is a full-stack application designed with the following architecture:

- **Frontend**: Built with React (or Next.js if migrated), it provides the user interface for the application.
- **Backend**: Powered by FastAPI, it serves as the API gateway and handles business logic.
- **Modules**:
  - **Interview Module**: Manages interview-related features and integrates with the Groq API.
  - **Auth Module**: Handles user authentication and authorization.
  - **Analytics Module**: Processes and provides metrics for the application.
- **Database**: PostgreSQL is used to store user data and other application-related information.
- **External Services**:
  - **Groq API**: Used for interview-related data.
  - **Metrics Engine**: Collects and analyzes analytics data.

---

## **Folder Structure**

Here’s a breakdown of the project structure:

### **Frontend**
Located in the `frontend/` folder, this is the user-facing part of the application.

- **`src/`**: Contains the main source code for the frontend.
  - **`components/`**: Reusable UI components like `InterviewSession`, `Results`, etc.
  - **`services/`**: Handles API calls to the backend.
- **`public/`**: Static files like `index.html` and `manifest.json`.
- **`package.json`**: Lists frontend dependencies.
- **`.env.example`**: Example environment variables for the frontend.

### **Backend**
Located in the `backend/` folder, this is the server-side logic of the application.

- **`main.py`**: The entry point for the backend application.
- **`Dockerfile`**: Instructions for building the backend Docker image.
- **`requirements.txt`**: Lists Python dependencies for the backend.
- **`modules/`**: Organized by features:
  - **`interview/`**: Handles interview-related logic.
    - **`routes.py`**: Defines API endpoints.
    - **`services.py`**: Contains business logic.
  - **`auth/`**: (To be added) Manages user authentication.
  - **`analytics/`**: (To be added) Processes metrics and analytics.
- **`config/`**: Stores configuration files.
- **`infrastructure/db/`**: Handles database models and repositories.

### **Shared**
Located in the `shared/` folder, this contains code shared across the project.

- **`errors.py`**: Defines custom error classes.
- **`result.py`**: Utility for handling operation results.

### **Tests**
Located in the `tests/` folder, this contains test cases for the application.

- **`domain/`**: Tests for domain logic, such as `test_user_entity.py`.

### **Docs**
Located in the `docs/` folder, this contains documentation for the project.

- **`architecture.md`**: Explains the system architecture.

---

## **How to Run the Project**

### **1. Prerequisites**
- Install **Docker** and **Docker Compose**.
- Install **Node.js** and **npm**.
- Install **Python 3.9+**.

### **2. Setup**

#### **Frontend**
1. Navigate to the `frontend/` folder.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

#### **Backend**
1. Navigate to the `backend/` folder.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

#### **Docker**
1. Build and run the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

---

## **Future Improvements**
- Add the **Auth Module** for user authentication.
- Add the **Analytics Module** for metrics and reporting.
- Migrate the frontend to **Next.js** for better SEO and performance.
- Integrate the **Groq API** into the Interview Module.
- Connect the **Metrics Engine** to the Analytics Module.

---

## **Contributing**
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## **Contact**
If you have any questions, feel free to reach out to the project maintainers.

Happy coding!
