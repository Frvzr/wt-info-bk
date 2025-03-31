from sqlalchemy import UUID, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class TemplateEquipment(Base):
    __tablename__ = "template_equipment"
    template_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('checklist_templates.id'), nullable=False, unique=False)
    equipment_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('equipment.id'), nullable=False, unique=False)
    is_active: Mapped[bool] = mapped_column(default=True)

    __table_args__ = (
        PrimaryKeyConstraint('template_id', 'equipment_id'),
    )
