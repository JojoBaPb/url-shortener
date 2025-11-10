from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings # Import our settings

# 1. Create the Async Engine
engine = create_async_engine(
    settings.database_url,
    echo=True,  # Log SQL queries (good for debugging)
)

# 2. Create the Session Maker
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False, # Keep objects accessible after commit
)

# 3. Create the Declarative Base
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
