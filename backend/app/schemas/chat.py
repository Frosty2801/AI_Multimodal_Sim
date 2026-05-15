from typing import Literal

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    session_id: str = Field(
        default="default",
        description="Conversation session identifier used to keep short-term memory.",
    )
    message: str = Field(..., min_length=1, description="User message sent to FinBot.")
    input_mode: Literal["text"] = "text"
    response_mode: Literal["text"] = "text"


class ChatResponse(BaseModel):
    session_id: str
    answer: str
    language: str = Field(
        default="auto",
        description="Language behavior is controlled by the model from the latest user message.",
    )
    cache_hit: bool = False
    tool_used: str | None = None
    rag_used: bool = False
    audio_url: str | None = None
    transcription: str | None = None
