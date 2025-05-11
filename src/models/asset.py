import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from ..models import Item


class Asset(Base):
    __tablename__ = "asset"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    serial_number: Mapped[String] = mapped_column(String(32), nullable=False, unique=True)
    equipment_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('item.id'), nullable=False, unique=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    status: Mapped[UUID] = mapped_column(UUID, ForeignKey('statuses.id'), nullable=True, unique=False)

    equipment: Mapped['Item'] = relationship(
        'Item',
        primaryjoin='Item.id == Asset.equipment_id',
        back_populates='asset',
        foreign_keys='Asset.equipment_id'
    )

    __table_args__ = {
        "comment": "Таблица с оборудованием (активами)"
    }
