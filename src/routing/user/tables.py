"""User related tables."""
from datetime import datetime
from sqlalchemy import Column, String

from src.database.database import Base


class User(Base):
    """User table model."""

    __tablename__ = "user"

    email = Column(String(100), primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    date_created = Column(String, nullable=False, default=datetime.now().isoformat)
    date_updated = Column(String, nullable=True, default=None, onupdate=datetime.now().isoformat)


user_table = User.__table__
