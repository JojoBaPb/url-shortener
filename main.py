from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import secrets
import string

import models, schemas, config
from database import engine, Base, get_db_session

# --- Database Setup ---

async def create_db_and_tables():
    """Create database tables on startup."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Create the FastAPI app instance
app = FastAPI()

@app.on_event("startup")
async def on_startup():
    """Run the create_db_and_tables function when the app starts."""
    await create_db_and_tables()
    
# --- Helper Functions ---

async def get_url_by_key(db: AsyncSession, key: str) -> models.URL | None:
    """
    Get a URL from the database by its short key.
    """
    result = await db.execute(
        select(models.URL).filter(models.URL.key == key)
    )
    return result.scalars().first()

async def create_unique_short_key(db: AsyncSession) -> str:
    """
    Generate a unique short key.
    """
    KEY_LENGTH = 7
    CHARS = string.ascii_letters + string.digits
    
    key = "".join(secrets.choice(CHARS) for _ in range(KEY_LENGTH))
    
    # Check if key already exists (very rare)
    if await get_url_by_key(db, key):
        return await create_unique_short_key(db) # Try again
    
    return key

# --- API Endpoints ---

@app.get("/")
async def root():
    """
    Root endpoint for a basic health check.
    """
    return {"message": "URL Shortener is running!"}


@app.get("/{short_key}")
async def forward_to_target_url(
    short_key: str,
    db: AsyncSession = Depends(get_db_session)
):
    """
    Looks up a short_key and redirects the user to the target_url.
    Also increments the click counter.
    """
    # 1. Look up the key in the database
    db_url = await get_url_by_key(db, short_key)

    if db_url is None:
        # 2. If not found, raise a 404 error
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"URL with key '{short_key}' not found."
        )

    # 3. Increment the click counter
    db_url.clicks += 1
    await db.commit()

    # 4. Return a redirect response
    return RedirectResponse(
        url=db_url.target_url, status_code=status.HTTP_307_TEMPORARY_REDIRECT
    )


@app.post("/create", response_model=schemas.URLInfo)
async def create_short_url(
    url_create: schemas.URLCreate,
    db: AsyncSession = Depends(get_db_session)
):
    """
    Create a new short URL.
    """
    # Create the unique key
    unique_key = await create_unique_short_key(db)
    
    # Create the new database model object
    db_url = models.URL(
        target_url=str(url_create.target_url), # Store as a string
        key=unique_key
    )
    
    # Add to the session and commit
    db.add(db_url)
    await db.commit()
    await db.refresh(db_url) # Get back the data we just saved (like the 'id')
    
    # Return the data, formatted by the `response_model`
    return db_url
