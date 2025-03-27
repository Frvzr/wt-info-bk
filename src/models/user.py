from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from ..models import Role, UserRole


class User(Base):
    """Модель пользователя"""
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(default=True)

    # Отношение через ассоциативную таблицу
    role_associations: Mapped[list["UserRole"]] = relationship(back_populates="user")

    # Свойство для удобного доступа к ролям
    @property
    def roles(self) -> list["Role"]:
        return [assoc.role for assoc in self.role_associations]

    def has_role(self, role_name: str) -> bool:
        return any(role.name == role_name for role in self.roles)

    def has_permission(self, permission: str) -> bool:
        return any(permission in role.permissions for role in self.roles)
