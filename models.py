from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from database import Base # Import the Base from database.py file

class URL(Base):
    """
    SQLAlchemy model for the 'urls' table.
    """
    __tablename__ = "urls"

    id = Column(BigInteger, primary_key=True, index=True)
    key = Column(String, unique=True, index=True)
    target_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)
