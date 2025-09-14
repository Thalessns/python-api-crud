"""Configs for database connections."""
from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    """Database configuration settings."""

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str


db_config = DatabaseConfig()
database_url = "sqlite+aiosqlite:///src/database/sqlite_db.db"
