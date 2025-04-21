from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func
from sqlalchemy import Integer

from src.models import RedressKit, RedressKitConsist, Item, ServiceLevel


class RedressKitRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list:
        query = await self.session.execute(
            select(
                Item.name.label('redress_kit'),
                Item.description,
                RedressKit.actual_revision,
                ServiceLevel.name.label('level')
            )
            .select_from(RedressKit)
            .join(Item)
            .join(ServiceLevel)
        )
        result = query.all()
        return list(result)

    async def get_redress_kit_with_items(self) -> list:
        Parent = aliased(Item, name='parent')
        Children = aliased(Item, name='children')

        query = (
            select(
                Parent.name.label('redress_kit'),
                Parent.description.label('desc_redress_kit'),
                Children.name.label('item'),
                Children.description.label('desc_item'),
                RedressKitConsist.quantity,
                RedressKitConsist.revision
            )
            .join(RedressKitConsist, Parent.id == RedressKitConsist.redress_kit_id)
            .join(Children, Children.id == RedressKitConsist.item_id)
        )

        result = await self.session.execute(query)
        return list(result)



    async def get_redress_kit_consist_by_id(self, redress_kit_id: str) -> list:
        Kit = aliased(Item, name="kit")
        Component = aliased(Item, name="component")

        hierarchy = (
            select(
                Kit.id.label("kit_id"),
                Kit.name.label("kit_name"),
                Component.id.label("component_id"),
                Component.name.label("component_name"),
                RedressKitConsist.quantity,
                RedressKitConsist.revision,
                func.cast(0, Integer).label("level")
            )
            .join(
                RedressKitConsist,
                Kit.id == RedressKitConsist.redress_kit_id
            )
            .join(
                Component,
                Component.id == RedressKitConsist.item_id
            )
            .where(Kit.id == redress_kit_id)
            .cte(name="hierarchy", recursive=True)
        )

        SubKit = aliased(Item, name="subkit")
        SubComponent = aliased(Item, name="subcomponent")

        hierarchy = hierarchy.union_all(
            select(
                SubKit.id.label("kit_id"),
                SubKit.name.label("kit_name"),
                SubComponent.id.label("component_id"),
                SubComponent.name.label("component_name"),
                RedressKitConsist.quantity,
                RedressKitConsist.revision,
                (hierarchy.c.level + 1).label("level")
            )
            .join(
                RedressKitConsist,
                SubKit.id == RedressKitConsist.redress_kit_id
            )
            .join(
                SubComponent,
                SubComponent.id == RedressKitConsist.item_id
            )
            .join(
                hierarchy,
                SubKit.id == hierarchy.c.component_id
            )
        )

        stmt = select(
            hierarchy.c.kit_id,
            hierarchy.c.kit_name,
            hierarchy.c.component_id,
            hierarchy.c.component_name,
            hierarchy.c.quantity,
            hierarchy.c.revision,
            hierarchy.c.level
        ).order_by(hierarchy.c.level)

        result = await self.session.execute(stmt)
        return list(result.all())
