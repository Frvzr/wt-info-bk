from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models import RedressKit, RedressKitConsist, Item, ServiceLevel


class RedressKitRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list:
        query = await self.session.execute(
            select(
                RedressKit.name.label('redress_kit'),
                RedressKit.description,
                ServiceLevel.name.label('level')
            )
            .select_from(RedressKit)
            .join(ServiceLevel)
        )
        result = query.all()
        return list(result)

    async def get_redress_kit_with_items(self) -> list:
        query = await self.session.execute(
            select(
                RedressKit.name.label('redress_kit'),
                RedressKit.description.label('desc_redress_kit'),
                Item.name.label('item'),
                Item.description.label('desc_item'),
                RedressKitConsist.quantity,
                RedressKitConsist.revision
            )
            .select_from(RedressKitConsist)
            .join(RedressKit)
            .join(Item)
        )
        result = query.all()
        return list(result)

    async def get_redress_kit_consist_by_name(self, name: str) -> list:
        query = await self.session.execute(
            select(
                Item.name.label('item'),
                Item.description.label('desc_item'),
                RedressKitConsist.quantity,
                RedressKitConsist.revision
            )
            .select_from(RedressKitConsist)
            .join(RedressKit)
            .join(Item)
            .where(RedressKit.name == name)
            )
        result = query.all()
        return list(result)
