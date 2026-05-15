from fastapi import FastAPI

from backend.app.api.chat import router as chat_router
from backend.app.api.health import router as health_router
from backend.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    debug=settings.app_debug,
)

app.include_router(health_router)
app.include_router(chat_router)