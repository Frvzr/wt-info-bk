from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID, ForeignKey, String, DateTime, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class RedressSteps(Base):
    __tablename__ = "redress_steps"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid4, unique=True)
    redress_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('redress_equipment.id'), nullable=False)
    step_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('checklist_steps.id'), nullable=False, unique=False)
    answer: Mapped[JSONB] = mapped_column(JSONB(), nullable=True)
    technician: Mapped[String] = mapped_column(String(32), nullable=True)
    completed_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    comment: Mapped[Text] = mapped_column(Text, nullable=True, unique=True)

    __table_args__ = {
        'comment': 'Таблица с ответами пользователей на шаги сервиса оборудования'
    }
