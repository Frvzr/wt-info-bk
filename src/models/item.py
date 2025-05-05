import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID, String, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from ..models import RedressKitConsist, Category


class Item(Base):
    __tablename__ = "item"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    name: Mapped[String] = mapped_column(String(32), nullable=False, unique=True)
    description: Mapped[String] = mapped_column(String(128), nullable=True)
    category_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('category.id'), nullable=True, unique=False)
    group_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('groups.id'), nullable=True, unique=False)
    source_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('sources.id'), nullable=True, unique=False)
    operation_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('operations.id'), nullable=True, unique=False)
    department_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('departments.id'), nullable=True, unique=False)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)

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

    redress_kit: Mapped[list['Item']] = relationship(
        'RedressKitConsist',
        primaryjoin='RedressKitConsist.redress_kit_id == Item.id',
        back_populates='redress_kit',
        foreign_keys='RedressKitConsist.redress_kit_id'
    )
    __table_args__ = (
        Index('ix_items_is_active', 'is_active'),
    )
