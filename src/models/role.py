from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from ..models import User, UserRole


class Role(Base):
    """Модель роли"""
    __tablename__ = 'roles'

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    permissions: Mapped[str] = mapped_column(String(500))  # JSON строка с разрешениями
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    # Отношение через ассоциативную таблицу
    user_associations: Mapped[list["UserRole"]] = relationship(back_populates="role")

    # Свойство для удобного доступа к пользователям
    @property
    def users(self) -> list["User"]:
        return [assoc.user for assoc in self.user_associations]