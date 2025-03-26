import uuid

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Equipment(Base):
    __tablename__ = "equipments"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    part_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('part.id'), nullable=False,  unique=False)
    tool_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('tool.id'), nullable=False,  unique=False)
    size_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('size.id'), nullable=True, unique=False)
    category_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('category.id'), nullable=True, unique=False)
