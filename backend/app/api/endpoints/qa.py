# app/api/endpoints/qa.py

from fastapi import APIRouter, Query, HTTPException
from app.services.qa_engine import qa_sessions

router = APIRouter()

@router.get("/ask/")
def ask_question(q: str = Query(...), session_id: str = Query(...)):
    if session_id not in qa_sessions:
        raise HTTPException(status_code=404, detail="Session ID not found.")
    
    answer = qa_sessions[session_id].ask(q)
    return {"answer": answer}
