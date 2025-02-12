import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from ..models import RedressKitConsist


class RedressKit(Base):
    __tablename__ = "redress_kit"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    name: Mapped[String] = mapped_column(String(32), nullable=False)
    description: Mapped[String] = mapped_column(String(128), nullable=True)
    service_level: Mapped[UUID] = mapped_column(UUID, nullable=False)   # Если одинаковый кит для двух уровней обслуживания, то надо делать связь m2m

    redress_kit: Mapped[list['RedressKitConsist']] = relationship(
        'RedressKitConsist',
        primaryjoin='RedressKit.id == RedressKitConsist.redress_kit_id',
        back_populates='redress_kit',
        foreign_keys='RedressKitConsist.redress_kit_id'
    )


