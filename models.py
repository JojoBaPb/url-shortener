from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from database import Base

class URL(Base):
    """
    SQLAlchemy model for the 'urls' table with Enterprise-Grade features.
    """
    __tablename__ = "urls"

    id = Column(BigInteger, primary_key=True, index=True)
    key = Column(String, unique=True, index=True) # The public short code
    secret_key = Column(String, unique=True, index=True, nullable=False) # The private management key
    target_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)
