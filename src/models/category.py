import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from ..models import Item


class Category(Base):
    __tablename__ = "category"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    name: Mapped[String] = mapped_column(String(32), nullable=False, unique=True)
    description: Mapped[String | None] = mapped_column(String(128), nullable=True)
    parent_category: Mapped[UUID | None] = mapped_column(UUID, ForeignKey("category.id"), nullable=True)

    item: Mapped['Item'] = relationship(
        'Item',
        primaryjoin='Item.category_id == Category.id',
        back_populates='category',
        foreign_keys='Item.category_id'
    )

    children: Mapped[list["Category"]] = relationship(back_populates="parent")
    parent: Mapped["Category"] = relationship(back_populates="children", remote_side=[id])
