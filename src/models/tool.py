import uuid

from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Tool(Base):
    __tablename__ = "tools"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    name: Mapped[String] = mapped_column(String(32), nullable=False)
    description: Mapped[String] = mapped_column(String(128), nullable=True)
