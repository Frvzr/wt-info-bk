import uuid

from sqlalchemy import UUID, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, unique=True, efault=uuid.uuid4)
    username: Mapped[String] = mapped_column(String(32), nullable=False, unique=True)
