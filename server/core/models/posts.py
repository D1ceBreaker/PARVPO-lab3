from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base


class Post(Base):
    author: Mapped[str] = mapped_column(ForeignKey("users.username"))
    title: Mapped[str] = mapped_column()
