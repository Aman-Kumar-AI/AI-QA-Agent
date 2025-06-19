# app/services/qa_engine.py

from llama_index.core import Settings, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from app.services.gemini_llm import GeminiLLM
from app.services.file_loader import load_documents

# 🔁 Store QASystems by session
qa_sessions = {}

class QASystem:
    def __init__(self, upload_dir: str):
        self.documents = load_documents(upload_dir)

        Settings.llm = GeminiLLM()
        Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

        self.index = VectorStoreIndex.from_documents(self.documents)
        self.query_engine = self.index.as_query_engine()

    def ask(self, query: str) -> str:
        return self.query_engine.query(query).response
