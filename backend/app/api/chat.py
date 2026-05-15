from fastapi import APIRouter, HTTPException

from backend.app.core.orchestrator import chat_orchestrator
from backend.app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    try:
        return chat_orchestrator.handle_chat(request)
    except Exception as error:
        raise HTTPException(
            status_code=502,
            detail=f"FinBot model provider error: {error}",
        ) from error
