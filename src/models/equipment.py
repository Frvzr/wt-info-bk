import uuid

from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Equipment(Base):
    __tablename__ = "equipment"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    part_number: Mapped[String] = mapped_column(String(32))
    description: Mapped[String] = mapped_column(String(256), nullable=True)
    tool_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('tool.id'), nullable=False,  unique=False)
    size_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('size.id'), nullable=True, unique=False)
    category_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('category.id'), nullable=True, unique=False)
