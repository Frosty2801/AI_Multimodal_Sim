from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_nvidia_ai_endpoints import ChatNVIDIA

from backend.app.core.prompts import FINBOT_SYSTEM_PROMPT
from backend.config import Settings


class FinBotAgent:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.llm = ChatNVIDIA(
            model=settings.nvidia_model,
            nvidia_api_key=settings.nvidia_api_key,
            base_url=settings.nvidia_base_url,
            temperature=settings.nvidia_temperature,
            max_completion_tokens=settings.nvidia_max_completion_tokens,
        )

    def respond(self, user_message: str, history: list[BaseMessage]) -> str:
        messages = [
            SystemMessage(content=FINBOT_SYSTEM_PROMPT),
            *history,
        ]

        if not history or history[-1].content != user_message:
            messages.append(HumanMessage(content=user_message))

        response = self.llm.invoke(messages)
        return str(response.content)
