import uuid

from sqlalchemy import String, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ChecklistTemplate(Base):
    __tablename__ = "checklist_templates"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    name: Mapped[String] = mapped_column(String(32), nullable=False)
    description: Mapped[String] = mapped_column(String(256), nullable=False)
    level: Mapped[UUID] = mapped_column(UUID, ForeignKey('service_level.id'), nullable=False)
    version: Mapped[String] = mapped_column(String(32), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
