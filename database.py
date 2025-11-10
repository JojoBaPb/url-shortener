from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, sessionmaker
from sqlalchemy.orm import declarative_base
from .config import settings

# 1. Create the Async Engine
# Engine is the central source of connectivity for the database.
# Use create_async_engine() for asyncio support.
engine = create_async_engine(
    settings.database_url,
    echo=True,  # Set to True to see the generated SQL queries in your console
)

# 2. Create the Session Maker
# This is a "factory" for creating new AsyncSession objects.
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False, # Keeps objects accessible after commit
)

# 3. Create the Declarative Base
# This is a base class that all our database models (tables) will inherit from.
# How SQLAlchemy knows what tables to create and how to map them to Python objects.
Base = declarative_base()

# 4. Dependency to get a DB session
async def get_db_session() -> AsyncSession:
    """
    FastAPI dependency to provide a database session.
    Ensures the session is always closed after the request.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
