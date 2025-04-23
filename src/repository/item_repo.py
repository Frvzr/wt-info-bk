from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models import Item, Category, Group, Source, Operation, Department


class ItemRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: dict) -> Item:
        item = Item(**data)
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def update(self, item_id: uuid4, data: dict) -> Item:
        result = await self.session.execute(
            select(Item).where(Item.id == item_id)
        )
        item = result.scalars().first()

        if not item:
            return None

        for key, value in data.items():
            setattr(item, key, value)

        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def patch(self, item_id: uuid4, data: dict) -> Item | None:
        result = await self.session.execute(
            select(Item).where(Item.id == item_id)
        )
        item = result.scalars().first()
        for key, value in data.items():
            if value == "":
                setattr(item, key, None)
            else:
                setattr(item, key, value)

        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def get_all(self):
        result = await self.session.execute(select(Item))
        return result.scalars().all()

    async def get_by_id(self, id: str) -> str | None:
        result = await self.session.execute(
            select(Item.id,
                   Item.name,
                   Item.description,
                   Category.name.label('category'),
                   Group.name.label('group'),
                   Source.name.label('source'),
                   Operation.name.label('operation'),
                   Department.name.label('department')
                   )
            .select_from(Item)
            .join(Category, isouter=True)
            .join(Group, isouter=True)
            .join(Source, isouter=True)
            .join(Operation, isouter=True)
            .join(Department, isouter=True)
            .where(Item.id == id)
        )
        print(result.all())
        return result.all()

    async def get_id_by_name(self, name: str) -> str | None:
        result = await self.session.execute(
            select(Item.id).where(Item.name == name)
        )
        item = result.scalars().first()
        return item if item else None

    async def get_items_with_category(self) -> list:
        query = (select(Item.id,
                        Item.name,
                        Item.description,
                        Category.name.label('category'),
                        Group.name.label('group'),
                        Source.name.label('source'),
                        Operation.name.label('operation'),
                        Department.name.label('department')
                        )
                 .select_from(Item)
                 .join(Category, isouter=True)
                 .join(Group, isouter=True)
                 .join(Source, isouter=True)
                 .join(Operation, isouter=True)
                 .join(Department, isouter=True)
                 )
        result = await self.session.execute(query)
        records = result.all()
        return list(records)
