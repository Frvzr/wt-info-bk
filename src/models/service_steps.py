from datetime import datetime

from sqlalchemy import UUID, ForeignKey, String, DateTime, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ServiceSteps(Base):
    __tablename__ = "service_steps"
    service_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('service_equipment.id'), nullable=False)
    step_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('checklist_steps.id'), nullable=False, unique=False)
    answer: Mapped[String] = mapped_column(String(300), nullable=True)
    technician: Mapped[String] = mapped_column(String(32), nullable=True)
    completed_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('service_id', 'step_id'),
    )
