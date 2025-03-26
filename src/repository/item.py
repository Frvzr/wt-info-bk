from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models import Item, Category


class ItemRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self):
        result = await self.session.execute(select(Item))

        return result.scalars().all()

    async def get_items_with_category(self) -> list:
        query = (select(Item.id,
                        Item.name.label('item_name'),
                        Item.description.label('item_description'),
                        Category.name.label('category_name'),
                        Category.description.label('category_description'))
                 .select_from(Item)
                 .join(Category, isouter=True))
        result = await self.session.execute(query)
        records = result.all()
        return list(records)

    async def create(self, item: Item):
        self.session.add(item)
        await self.session.flush()
        await self.session.commit()