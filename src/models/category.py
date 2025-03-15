import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from ..models import Item


class Category(Base):
    __tablename__ = "category"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    name: Mapped[String] = mapped_column(String(32), nullable=False)
    description: Mapped[String] = mapped_column(String(128), nullable=True)

    item: Mapped['Item'] = relationship(
        'Item',
        primaryjoin='Item.id == Category.id',
        back_populates='category',
        foreign_keys='Category.id'
    )
