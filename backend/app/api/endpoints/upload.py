# app/api/endpoints/upload.py

from fastapi import APIRouter, UploadFile, File, Form
import shutil
import os
import uuid
from app.services.qa_engine import QASystem, qa_sessions


router = APIRouter()
UPLOAD_DIR = "app/uploads"
q="You are a summarizer and you need to summarize the document clearly"
@router.post("/upload/")
async def upload_file(file: UploadFile = File(...), session_id: str = Form(None)):
    # Generate session ID if not provided
    if not session_id:
        session_id = str(uuid.uuid4())

    session_path = os.path.join(UPLOAD_DIR, session_id)
    
    os.makedirs(session_path, exist_ok=True)

    file_path = os.path.join(session_path, file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Rebuild index for this session
    qa_sessions[session_id] = QASystem(session_path)
    summary = qa_sessions[session_id].ask(q)
    return {
        "message": f"File '{file.filename}' uploaded and indexed successfully.",
        "session_id": session_id,
        "summary":summary
    }
