from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

# 1. Create the Async Engine (one for the whole app; it keeps a pool of connections)
engine = create_async_engine(settings.database_url, echo=settings.sql_echo)

# 2. Create the Session Maker (expire_on_commit=False keeps objects usable after commit)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


# 3. Create the Declarative Base
class Base(DeclarativeBase):
    """Parent class for all database tables."""


# 4. Dependency to get a DB session
async def get_db_session() -> AsyncIterator[AsyncSession]:
    """
    FastAPI dependency to provide a database session.
    Ensures the session is always closed after the request.
    """
    async with SessionLocal() as session:
        yield session
