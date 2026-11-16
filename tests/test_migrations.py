"""Migrations must (1) run up and down cleanly and (2) build exactly what the models describe.

Test (2) catches "drift": someone changes a model but forgets to write a migration.
"""

import asyncio
import tempfile
from pathlib import Path

from alembic import command
from alembic.autogenerate import compare_metadata
from alembic.config import Config
from alembic.migration import MigrationContext
from sqlalchemy.ext.asyncio import create_async_engine

from app.database import Base


def _alembic_config(url: str) -> Config:
    cfg = Config("alembic.ini")
    cfg.set_main_option("sqlalchemy.url", url)
    return cfg


def _fresh_sqlite_url() -> str:
    path = Path(tempfile.mkdtemp()) / "migrations.db"
    return f"sqlite+aiosqlite:///{path.as_posix()}"


async def test_upgrade_then_downgrade_runs_cleanly():
    cfg = _alembic_config(_fresh_sqlite_url())
    # Alembic starts its own event loop, so run it in a worker thread.
    await asyncio.to_thread(command.upgrade, cfg, "head")
    await asyncio.to_thread(command.downgrade, cfg, "base")
    await asyncio.to_thread(command.upgrade, cfg, "head")


async def test_models_and_migrations_match():
    url = _fresh_sqlite_url()
    await asyncio.to_thread(command.upgrade, _alembic_config(url), "head")

    engine = create_async_engine(url)
    async with engine.connect() as conn:
        differences = await conn.run_sync(
            lambda sync_conn: compare_metadata(MigrationContext.configure(sync_conn), Base.metadata)
        )
    await engine.dispose()

    assert differences == [], f"Models changed without a migration: {differences}"
