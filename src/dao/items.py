from .base import BaseDAO
from src.models.item import Item
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class ItemDAO(BaseDAO):
    model = Item

    @classmethod
    async def add_item(cls, session: AsyncSession, item_data: dict) -> Item:
        """
            Добавляет item с категорией.

            Аргументы:
            - session: AsyncSession - асинхронная сессия базы данных
            - item_data: dict - словарь с данными

            Возвращает:
            - Item - объект item
        """
        item = cls.model(
            name=item_data['name'],
            description=item_data['description'],
            category=item_data['category']
        )
        session.add(item)
        await session.flush()

        await session.commit()

        return item

    @classmethod
    async def get_all_items(cls, session: AsyncSession):
        # Создаем запрос для выборки всех пользователей
        query = select(cls.model)

        # Выполняем запрос и получаем результат
        result = await session.execute(query)

        # Извлекаем записи как объекты модели
        records = result.scalars().all()

        return records
