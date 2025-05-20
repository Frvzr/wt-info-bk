from datetime import datetime
from uuid import uuid4
from sqlalchemy import UUID, ForeignKey, DateTime, Text, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class RedressEquipment(Base):
    __tablename__ = "redress_equipment"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid4, unique=True)
    asset_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('asset.id'), nullable=False, unique=False)
    level_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('service_level.id'), nullable=True, unique=False)
    template_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('template_equipment.id'), nullable=True, unique=False)
    tag_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('statuses.id'), nullable=True, unique=False)
    # assigned_to: Mapped[UUID] = mapped_column(UUID, ForeignKey('users.id'), nullable=False, unique=False)
    assigned_to: Mapped[String] = mapped_column(String(32), nullable=False, unique=False)
    top_tool: Mapped[UUID] = mapped_column(UUID, ForeignKey('asset.id'), nullable=True, unique=False)
    completed_to: Mapped[String] = mapped_column(String(32), nullable=True, unique=False)
    location_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('location.id'), nullable=False, unique=False)
    completed_date: Mapped[datetime] = mapped_column(DateTime, nullable=True, unique=False)
    status: Mapped[String] = mapped_column(String(16), nullable=False, default='draft')
    comment: Mapped[Text] = mapped_column(Text, nullable=True, unique=False)

    __table_args__ = {
        'comment': 'Таблица с проведенным редресом оборудованием'
    }
