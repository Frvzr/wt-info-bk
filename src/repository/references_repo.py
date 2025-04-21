from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models import Category, Group, Source, Operation, Department


class CategoryRepository:
    def __init__ (self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list:
        query = (select(Category.id,
                        Category.name)
                 .select_from(Category))

        category = await self.session.execute(query)
        result = category.all()
        return list(result)
