from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True, primary_key=True)