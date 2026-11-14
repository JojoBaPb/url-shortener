from sqlalchemy import BigInteger, Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

# SQLite only auto-numbers a primary key when its type is exactly INTEGER,
# so we use BIGINT on PostgreSQL and INTEGER on SQLite.
BigIntId = BigInteger().with_variant(Integer(), "sqlite")


class URL(Base):
    """One row per shortened link.

    The columns are kept exactly as the original table, including which ones may be
    empty (the "| None" ones). A later stage tightens these rules with a migration.
    """

    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(BigIntId, primary_key=True, index=True)
    key: Mapped[str | None] = mapped_column(String, unique=True, index=True)  # public short code
    secret_key: Mapped[str] = mapped_column(String, unique=True, index=True)  # private admin key
    target_url: Mapped[str | None] = mapped_column(String, index=True)
    is_active: Mapped[bool | None] = mapped_column(Boolean, default=True)
    clicks: Mapped[int | None] = mapped_column(Integer, default=0)
