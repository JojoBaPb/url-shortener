from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """All settings come from environment variables or a .env file.

    Every setting has a safe default so the app starts on a laptop with zero setup
    (it uses a local SQLite file). In production you override them, for example
    DATABASE_URL=postgresql+asyncpg://user:password@host:5432/dbname
    """

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "sqlite+aiosqlite:///./shortener.db"
    # Printing every SQL query is useful while debugging, but slow and noisy in production.
    sql_echo: bool = False


settings = Settings()
