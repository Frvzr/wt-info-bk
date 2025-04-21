import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from ..models import RedressKitConsist, Item


class RedressKit(Base):
    __tablename__ = "redress_kit"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    redress_kit: Mapped[UUID] = mapped_column(UUID, ForeignKey('item.id'), nullable=False)
    service_level: Mapped[UUID] = mapped_column(UUID, ForeignKey('service_level.id'), nullable=False)
    actual_revision: Mapped[String] = mapped_column(String(32), nullable=False)
    #
    # redress_kit_consist: Mapped[list['RedressKitConsist']] = relationship(
    #     'RedressKitConsist',
    #     primaryjoin='RedressKit.id == RedressKitConsist.redress_kit_id',
    #     back_populates='redress_kit',
    #     foreign_keys='RedressKitConsist.redress_kit_id'
    # )
    #
    # item: Mapped[list['Item']] = relationship(
    #     'Item',
    #     primaryjoin='RedressKit.redress_kit == Item.id',
    #     back_populates='redress_kit',
    #     foreign_keys='RedressKit.redress_kit'
    # )