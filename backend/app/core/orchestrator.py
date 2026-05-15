from backend.app.core.agent import FinBotAgent
from backend.app.core.memory import session_memory
from backend.app.schemas.chat import ChatRequest, ChatResponse
from backend.config import get_settings


class ChatOrchestrator:
    def __init__(self) -> None:
        self.settings = get_settings()
        self._agent: FinBotAgent | None = None

    @property
    def agent(self) -> FinBotAgent:
        if self._agent is None:
            self._agent = FinBotAgent(self.settings)
        return self._agent

    def handle_chat(self, request: ChatRequest) -> ChatResponse:
        history = session_memory.get_messages(request.session_id)

        answer = self.agent.respond(
            user_message=request.message,
            history=history,
        )

        session_memory.add_user_message(request.session_id, request.message)
        session_memory.add_ai_message(request.session_id, answer)

        return ChatResponse(
            session_id=request.session_id,
            answer=answer,
            language="auto",
        )


chat_orchestrator = ChatOrchestrator()
