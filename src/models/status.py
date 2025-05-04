import uuid

from sqlalchemy import UUID, String, BOOLEAN
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Status(Base):
    __tablename__ = "statuses"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False,  default=uuid.uuid4, unique=True)
    name: Mapped[String] = mapped_column(String(32), nullable=False, unique=True)
    description: Mapped[String] = mapped_column(String(256), nullable=True)
    is_active: Mapped[BOOLEAN] = mapped_column(BOOLEAN, default=True)
