from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select, update


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

    async def update(self, item_id: UUID, data: dict) -> Item | None:
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

    async def patch(self, item_id: UUID, data: dict) -> Item | None:
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
        result = await self.session.execute(select(Item).where(Item.is_active == "True"))
        return result.scalars().all()

    async def get_by_id(self, id: UUID) -> Item | None:
        result = await self.session.execute(
            select(
                Item.id,
                Item.name,
                Item.description,
                Item.category_id,
                Item.group_id,
                Item.source_id,
                Item.operation_id,
                Item.department_id)
            .select_from(Item)
            .where(Item.id == id)
        )
        return result.mappings().first()

    async def get_item_with_info_by_id(self, id: UUID) -> Item | None:
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
        return result.mappings().first()

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

    async def delete_item(self, id: UUID) -> bool:
        try:
            item = delete(Item).where(Item.id == id)
            result = await self.session.execute(item)
            await self.session.commit()
            return result.rowcount > 0
        except Exception as e:
            await self.session.rollback()
            raise ValueError(f"Delete failed: {str(e)}")

    async def mark_delete(self, item_id: UUID) -> bool:
        query = (update(Item)
                  .where(Item.id == item_id)
                  .values(is_active=False)
                  .execution_options(synchronize_session="fetch")
                 )
        item = await self.session.execute(query)
        await self.session.commit()
        return item
