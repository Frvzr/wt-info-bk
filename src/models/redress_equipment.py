from datetime import datetime
from uuid import uuid4
from sqlalchemy import UUID, ForeignKey, DateTime, Text, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class RedressEquipment(Base):
    __tablename__ = "redress_equipment"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid4, unique=True)
    asset_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('asset.id'), nullable=False, unique=False)
    template_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('template_equipment.id'), nullable=True, unique=False)
    tag: Mapped[UUID] = mapped_column(UUID, ForeignKey('statuses.id'), nullable=False, unique=False)
    # assigned_to: Mapped[UUID] = mapped_column(UUID, ForeignKey('users.id'), nullable=False, unique=False)
    assigned_to: Mapped[String] = mapped_column(String(32), nullable=False, unique=True)
    completed_to: Mapped[String] = mapped_column(String(32), nullable=False, unique=True)
    location: Mapped[UUID] = mapped_column(UUID, ForeignKey('location.id'), nullable=False)
    completed_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    status: Mapped[String] = mapped_column(String(16), nullable=False, default='draft')
    comment: Mapped[Text] = mapped_column(Text, nullable=True, unique=True)

    __table_args__ = {
        'comment': 'Таблица с оборудованием после обслуживания'
    }
