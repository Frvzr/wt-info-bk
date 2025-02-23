from .base import BaseDAO
from src.models.item import Item
from sqlalchemy.ext.asyncio import AsyncSession
from database import connection
from asyncio import run


class ItemDAO(BaseDAO):
    model = Item

    @classmethod
    async def add_item(cls, session: AsyncSession, item_data: dict) -> Item:
        """
                Добавляет пользователя и привязанный к нему профиль.

                Аргументы:
                - session: AsyncSession - асинхронная сессия базы данных
                - item_data: dict - словарь с данными пользователя и профиля

                Возвращает:
                - Item - объект item
                """
        item = cls.model(
            name=item_data['name'],
            description=item_data['description']
        )
        session.add(item)
        await session.flush()

        await session.commit()

        return item
