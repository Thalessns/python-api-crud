"""Entrypoint to run the API."""
import uvicorn

from pydantic_settings import BaseSettings


class EntrypointConfig(BaseSettings):
    APP_HOST: str
    APP_PORT: int


config = EntrypointConfig()

uvicorn.run(
    app="src.app.main:app",
    host=config.APP_HOST,
    port=config.APP_PORT,
    reload=False,
    log_level="info"
)