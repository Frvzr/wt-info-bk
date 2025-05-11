from sqlalchemy import UUID, ForeignKey, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4
from .base import Base


class TemplateSteps(Base):
    __tablename__ = "template_steps"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid4, unique=True)
    template_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('checklist_templates.id'), nullable=False, unique=False)
    step_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('checklist_steps.id'), nullable=False, unique=False)
    order: Mapped[Integer] = mapped_column(Integer, nullable=False, unique=False)
    is_mandatory: Mapped[bool] = mapped_column(Boolean, default=True)

    __table_args__ = {
        'comment': 'Дополнительная таблица шаблон - шаг'
    }
