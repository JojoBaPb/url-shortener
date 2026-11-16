"""Shared test setup.

Tests use a throwaway SQLite file by default, so they run anywhere with no database
installed. To run the same tests against PostgreSQL, set DATABASE_URL before running
pytest (CI does this).
"""

import os
import tempfile
from pathlib import Path

# This must happen BEFORE the app is imported, because app.config reads it at import time.
_test_db = Path(tempfile.mkdtemp()) / "test.db"
os.environ.setdefault("DATABASE_URL", f"sqlite+aiosqlite:///{_test_db.as_posix()}")

import pytest  # noqa: E402
from httpx import ASGITransport, AsyncClient  # noqa: E402

from app.database import Base, engine  # noqa: E402
from app.main import app  # noqa: E402


@pytest.fixture(autouse=True)
async def fresh_database():
    """Every test starts with empty tables, so tests can't affect each other."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Close pooled connections so the next test (which gets a new event loop) starts clean.
    await engine.dispose()


@pytest.fixture
async def client():
    """An HTTP client that talks to the app in memory: no server, no network."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c


@pytest.fixture
async def created(client):
    """A link that already exists, for tests that need one."""
    response = await client.post("/create", json={"target_url": "https://example.com/page"})
    assert response.status_code == 200
    return response.json()
