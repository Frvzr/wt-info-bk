from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models.item import Item

class ItemRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self):
        result = await self.session.execute(select(Item))

        return result.scalars().all()
