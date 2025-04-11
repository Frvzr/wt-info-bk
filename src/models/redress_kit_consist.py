from typing import TYPE_CHECKING

from sqlalchemy import String, PrimaryKeyConstraint, UUID, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from ..models import RedressKit, Item


class RedressKitConsist(Base):
    __tablename__ = "redress_kit_consist"
    redress_kit_id: Mapped[UUID] = mapped_column(UUID, nullable=False, comment="Идентификационный номер набора ЗИП")
    item_id: Mapped[UUID] = mapped_column(UUID, nullable=False, comment="Идентификационный номер ЗИП")
    quantity: Mapped[Float] = mapped_column(Float, nullable=False, comment="Количество")
    revision: Mapped[String] = mapped_column(String(32), nullable=False, comment="Версия набора ЗИП")

    redress_kit: Mapped[list['RedressKit']] = relationship(
        'RedressKit',
        primaryjoin='RedressKit.id == RedressKitConsist.redress_kit_id',
        back_populates='redress_kit_consist',
        foreign_keys='RedressKitConsist.redress_kit_id'
    )

    item: Mapped[list['Item']] = relationship(
        'Item',
        primaryjoin='Item.id == RedressKitConsist.item_id',
        back_populates='redress_kit_consist',
        foreign_keys='RedressKitConsist.item_id'
    )

    __table_args__ = (
        PrimaryKeyConstraint('redress_kit_id', 'item_id', 'revision'),
    )
