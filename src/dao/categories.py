from .base import BaseDAO
from src.models.category import Category
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class CategoryDAO(BaseDAO):
    model = Category

    @classmethod
    async def add_category(cls, session: AsyncSession, data: dict) -> Category:
        """
            Добавляет item с категорией.

            Аргументы:
            - session: AsyncSession - асинхронная сессия базы данных
            - data: dict - словарь с данными

            Возвращает:
            - Category- объект категории
        """
        category = cls.model(
            name=data['name'],
            description=data['description']
        )
        session.add(category)
        await session.flush()

        await session.commit()

        return category