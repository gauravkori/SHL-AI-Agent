from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.recommender import chat

router = APIRouter()


class ChatRequest(BaseModel):
    session_id: str
    message: str


@router.get("/health")
def health():
    return {
        "status": "ok"
    }


@router.post("/chat")
def chat_api(request: ChatRequest):

    return chat(
        session_id=request.session_id,
        message=request.message
    )