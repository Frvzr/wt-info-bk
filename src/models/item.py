import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from ..models import RedressKitConsist


class Item(Base):
    __tablename__ = "item"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    name: Mapped[String] = mapped_column(String(32), nullable=False)
    description: Mapped[String] = mapped_column(String(128), nullable=True)

    redress_kit_consist: Mapped[list['RedressKitConsist']] = relationship(
        'RedressKitConsist',
        primaryjoin='Item.id == RedressKitConsist.item_id',
        back_populates='item',
        foreign_keys='RedressKitConsist.item_id'
    )
