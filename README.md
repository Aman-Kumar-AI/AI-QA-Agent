# 🤖 AI QA Agent – Document Question Answering App

An AI-powered web application that allows users to upload documents and interact with them through natural language questions. Built with a modern Angular standalone frontend and a FastAPI backend using LlamaIndex + Gemini for intelligent answers.

---

## 📁 Project Structure

AI-QA-Agent/
├── backend/ # FastAPI app with Gemini + LlamaIndex integration
├── frontend/ # Angular standalone UI (no AppModule)
└── README.md # You're here


---

## 🧠 Features

- Upload documents in `.txt`, `.pdf`, `.docx`, `.csv`, `.xlsx` formats
- Generate a file summary instantly
- Ask questions about the uploaded document using Gemini (Google AI)
- Maintains sessions using `session_id` for continuity
- Clean, modern UI with green-yellow gradient and glassmorphism ✨

---

## 🚀 Getting Started

### ✅ Backend Setup (FastAPI + Gemini + LlamaIndex)

> Requirements: Python 3.9+, virtualenv, pip

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Use `venv\Scripts\activate` on Windows
pip install -r requirements.txt

# Create .env file and add your Gemini API key
echo "GEMINI_API_KEY=your-gemini-api-key-here" > .env

# Start the backend server
uvicorn app.main:app --reload

📡 API runs at: http://localhost:8000

✅ Frontend Setup (Angular Standalone App)
Requirements: Node.js (v18+), Angular CLI

cd frontend
npm install
ng serve

🌐 UI runs at: http://localhost:4200

🔐 Environment Variables
In the backend/.env file:

GEMINI_API_KEY=your-gemini-api-key


You can get your free Gemini API key from https://makersuite.google.com/app/apikey

🛠 Tech Stack
Layer	Tech
Frontend	Angular 17 (Standalone API, Vite)
Styling	Glassmorphism, CSS Gradient
Backend	FastAPI
AI Engine	Gemini Pro (Google Generative AI)
NLP Toolkit	LlamaIndex + HuggingFace Embeddings
Uploads	FileReader + Llama Parsers
Session Mgmt	session_id-based Q&A isolation

📷 Screenshots
Coming soon: UI previews of upload, summary, Q&A flow

👨‍💻 Developer Notes
Files are uploaded into backend/app/uploads/

Each session has its own vector index built on upload

UI resets gracefully when new document is uploaded

📌 To-Do / Enhancements
 Drag-and-drop upload UI

 Chat-style interface with history

 Support for image-based OCR (optional)

 Deployment with Docker / Render / Vercel

📄 License
MIT License – © 2025 Aman Kumar