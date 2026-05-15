
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(default="FinBot", alias="APP_NAME")
    app_env: str = Field(default="development", alias="APP_ENV")
    app_debug: bool = Field(default=True, alias="APP_DEBUG")

    backend_host: str = Field(default="127.0.0.1", alias="BACKEND_HOST")
    backend_port: int = Field(default=8000, alias="BACKEND_PORT")

    nvidia_api_key: str = Field(default="", alias="NVIDIA_API_KEY")
    nvidia_model: str = Field(
        default="meta/llama-3.1-70b-instruct",
        alias="NVIDIA_MODEL",
    )

    semantic_cache_threshold: float = Field(default=0.90, alias="SEMANTIC_CACHE_THRESHOLD")
    rag_chunk_size: int = Field(default=1000, alias="RAG_CHUNK_SIZE")
    rag_chunk_overlap: int = Field(default=150, alias="RAG_CHUNK_OVERLAP")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
