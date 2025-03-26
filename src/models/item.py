import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from ..models import RedressKitConsist, Category


class Item(Base):
    __tablename__ = "items"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    name: Mapped[String] = mapped_column(String(32), nullable=False, unique=True)
    description: Mapped[String] = mapped_column(String(128), nullable=True)
    category_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('category.id'), nullable=True, unique=False)

    redress_kit_consist: Mapped[list['RedressKitConsist']] = relationship(
        'RedressKitConsist',
        primaryjoin='Item.id == RedressKitConsist.item_id',
        back_populates='item',
        foreign_keys='RedressKitConsist.item_id'
    )

    category: Mapped['Category'] = relationship(
        'Category',
        primaryjoin='Item.id == Category.id',
        back_populates='item',
        foreign_keys='Category.id'
    )
