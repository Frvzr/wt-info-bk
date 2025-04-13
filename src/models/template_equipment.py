from uuid import uuid4
from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class TemplateEquipment(Base):
    __tablename__ = "template_equipment"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid4, unique=True)
    template_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('checklist_templates.id'), nullable=False, unique=False)
    equipment_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('equipment.id'), nullable=False, unique=False)
    is_active: Mapped[bool] = mapped_column(default=True)
