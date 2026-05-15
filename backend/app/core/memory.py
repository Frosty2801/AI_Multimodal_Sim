from collections import defaultdict, deque
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage

class SessionMemory:
    def __init__(self, max_messages: int = 7) -> None:
        self.max_messages = max_messages
        self._messages: dict[str, deque[BaseMessage]] = defaultdict(
            lambda: deque(maxlen=self.max_messages)
        )

    def get_messages(self,session_id: str) -> list[BaseMessage]:
        return list(self._messages[session_id])
    
    def add_user_message(self, session_id: str, content: str) -> None:
        self._messages[session_id].append(HumanMessage(content=content))

    def add_ai_message(self, session_id: str, content: str) -> None:
        self._messages[session_id].append(AIMessage(content=content))

    def clear(self, session_id: str) -> None:
        self._messages.pop(session_id, None)


session_memory = SessionMemory()