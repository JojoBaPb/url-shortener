from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
import models, schemas, keygen

async def get_db_url_by_key(db: AsyncSession, key: str) -> models.URL | None:
    result = await db.execute(select(models.URL).filter(models.URL.key == key))
    return result.scalars().first()

async def get_db_url_by_secret_key(db: AsyncSession, secret_key: str) -> models.URL | None:
    """Retrieves a URL record using the private secret key."""
    result = await db.execute(select(models.URL).filter(models.URL.secret_key == secret_key))
    return result.scalars().first()

async def create_db_url(db: AsyncSession, url: schemas.URLCreate) -> models.URL:
    """Generates both a short code and a secret key, then saves to DB."""
    # Generate unique short code
    while True:
        key = keygen.create_random_key()
        if not await get_db_url_by_key(db, key):
            break
            
    # Generate unique secret key
    while True:
        secret_key = keygen.create_unique_random_key()
        if not await get_db_url_by_secret_key(db, secret_key):
            break

    db_url = models.URL(
        target_url=str(url.target_url),
        key=key,
        secret_key=secret_key
    )
    db.add(db_url)
    await db.commit()
    await db.refresh(db_url)
    return db_url

async def delete_db_url(db: AsyncSession, secret_key: str) -> bool:
    """Permanently removes a URL record from the database (GDPR Compliance)."""
    db_url = await get_db_url_by_secret_key(db, secret_key)
    if db_url:
        await db.delete(db_url)
        await db.commit()
        return True
    return False
