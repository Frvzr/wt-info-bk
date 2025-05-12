import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from src.models import Item


class Type(Base):
    __tablename__ = "types"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    name: Mapped[String] = mapped_column(String(32), nullable=False)
    description: Mapped[String] = mapped_column(String(128), nullable=True)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)

    item: Mapped['Item'] = relationship(
        'Item',
        primaryjoin='Item.type_id == Type.id',
        back_populates='item',
        foreign_keys='Item.type_id'
    )
