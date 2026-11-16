from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, schemas
from app.database import engine, get_db_session


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # Tables are created by migrations (alembic upgrade head), not here.
    yield
    # Runs once when the server stops: close every pooled database connection cleanly.
    await engine.dispose()


app = FastAPI(title="Enterprise URL Shortener", lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Enterprise URL Shortener is online."}


@app.post("/create", response_model=schemas.URLInfo)
async def create_short_url(
    url_create: schemas.URLCreate, db: AsyncSession = Depends(get_db_session)
):
    return await crud.create_db_url(db, url_create)


@app.get("/stats/{secret_key}", response_model=schemas.URLInfo)
async def get_url_stats(secret_key: str, db: AsyncSession = Depends(get_db_session)):
    """Retrieve stats using the secret_key."""
    db_url = await crud.get_db_url_by_secret_key(db, secret_key)
    if not db_url:
        raise HTTPException(status_code=404, detail="Invalid secret key")
    return db_url


@app.delete("/admin/{secret_key}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_url(secret_key: str, db: AsyncSession = Depends(get_db_session)):
    """Right to be forgotten: physically removes the data from the database."""
    success = await crud.delete_db_url(db, secret_key)
    if not success:
        raise HTTPException(status_code=404, detail="Secret key not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# The catch-all redirect route goes LAST so it can never swallow another route.
@app.get("/{short_key}")
async def forward_to_target_url(short_key: str, db: AsyncSession = Depends(get_db_session)):
    db_url = await crud.get_db_url_by_key(db, short_key)
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")

    db_url.clicks += 1
    await db.commit()
    return RedirectResponse(url=db_url.target_url)
