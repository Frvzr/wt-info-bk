from datetime import datetime
from uuid import uuid4
from sqlalchemy import UUID, ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ServiceEquipment(Base):
    __tablename__ = "service_equipment"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid4, unique=True)
    asset_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('asset.id'), nullable=False, unique=False)
    template_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('template_equipment.id'), nullable=False, unique=False)
    level: Mapped[UUID] = mapped_column(UUID, ForeignKey('service_level.id'), nullable=False)
    location: Mapped[UUID] = mapped_column(UUID, ForeignKey('location.id'), nullable=False)
    completed_technician: Mapped[String] = mapped_column(String(32), nullable=False)
    completed_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    is_completed: Mapped[bool] = mapped_column(default=False)
