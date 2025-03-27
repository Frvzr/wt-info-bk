from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import UUID, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from ..models import User, Role


class UserRole(Base):
    """Ассоциативная таблица между User и Role с дополнительными атрибутами"""
    __tablename__ = 'user_role'

    user_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('users.id'), primary_key=True)
    role_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('roles.id'), primary_key=True)
    assigned_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    assigned_by: Mapped[str] = mapped_column(String(100), nullable=True)  # Кто назначил роль

    # Отношения
    user: Mapped["User"] = relationship(back_populates="role_associations")
    role: Mapped["Role"] = relationship(back_populates="user_associations")