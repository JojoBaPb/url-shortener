"""Create the urls table exactly as the original app created it.

Revision ID: 0001
Revises:
Create Date: 2026-11-13

If you already have a database that the old code created (with create_all), don't
run this migration; mark it as done instead:   alembic stamp 0001
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "urls",
        sa.Column(
            "id",
            sa.BigInteger().with_variant(sa.Integer(), "sqlite"),
            primary_key=True,
        ),
        sa.Column("key", sa.String(), nullable=True),
        sa.Column("secret_key", sa.String(), nullable=False),
        sa.Column("target_url", sa.String(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("clicks", sa.Integer(), nullable=True),
    )
    op.create_index("ix_urls_id", "urls", ["id"])
    op.create_index("ix_urls_key", "urls", ["key"], unique=True)
    op.create_index("ix_urls_secret_key", "urls", ["secret_key"], unique=True)
    op.create_index("ix_urls_target_url", "urls", ["target_url"])


def downgrade() -> None:
    op.drop_index("ix_urls_target_url", table_name="urls")
    op.drop_index("ix_urls_secret_key", table_name="urls")
    op.drop_index("ix_urls_key", table_name="urls")
    op.drop_index("ix_urls_id", table_name="urls")
    op.drop_table("urls")
