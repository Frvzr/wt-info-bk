from typing import Annotated
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    uniq_str_an = Annotated[str, mapped_column(unique=True)]

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return "cls.__name__.lower()"
