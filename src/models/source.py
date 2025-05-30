import uuid

from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Source(Base):
    __tablename__ = "sources"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    description: Mapped[String] = mapped_column(String(512), nullable=True, unique=False)
    name: Mapped[String] = mapped_column(String(32), nullable=False, unique=True)
    is_active: Mapped[bool] = mapped_column(default=True)
