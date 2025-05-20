from uuid import UUID
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models import (RedressEquipment, Asset, ServiceLevel, Location, TemplateEquipment,
                        ChecklistTemplate, Item, ChecklistSteps, RedressSteps, Status)


class RedressEquipmentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[RedressEquipment]:
        query = await self.session.execute(
            select(RedressEquipment.id,
                   Asset.serial_number,
                   ServiceLevel.name.label('level'),
                   Location.name.label('location'),
                   RedressEquipment.completed_to.label('alias'),
                   RedressEquipment.completed_date,
                   RedressEquipment.status)
            .select_from(RedressEquipment)
            .join(Asset, isouter=True)
            .join(ServiceLevel)
            .join(Location)
        )
        result = query.all()
        return list(result)

    async def get_user_redresses(self, username: str) -> list[RedressEquipment]:
        result = await self.session.execute(
            select(RedressEquipment)
            .where(RedressEquipment.completed_to == username)
            .order_by(RedressEquipment.completed_date.desc())
        )
        return list(result.scalars().all())

    async def get_template_by_level(self, equipment_id: UUID, level_id: UUID) -> ChecklistTemplate | None:
        result = await self.session.execute(
            select(ChecklistTemplate)
            .join(TemplateEquipment, TemplateEquipment.template_id == ChecklistTemplate.id)
            .where(
                TemplateEquipment.equipment_id == equipment_id,
                ChecklistTemplate.level_id == level_id,
                ChecklistTemplate.is_active
            )
        )
        return result.scalar_one_or_none()

    async def get_redress_by_id(self, redress_id: UUID) -> list:
        query = await self.session.execute(
            select(
                    ChecklistSteps.name.label('step'),
                    ChecklistSteps.description,
                    RedressSteps.answer,
                    RedressSteps.technician,
                    RedressSteps.completed_date
                   )
            .select_from(RedressSteps)
            .join(ChecklistSteps)
            .where(RedressEquipment.id == redress_id)
        )
        result = query.all()
        return list(result)

    async def get_redress_history(self, asset_id: UUID | None = None) -> list[RedressEquipment] | None:
        query = (
            select(
                RedressEquipment.id,
                Asset.serial_number,
                Item.name.label('part_number'),
                Status.name.label('tag'),
                RedressEquipment.completed_to,
                RedressEquipment.completed_date,
                Location.name.label('location')
            )
                .select_from(RedressEquipment)
        )

        query = (
            query
            .join(Asset, Asset.id == RedressEquipment.asset_id)
            .join(Item, Asset.equipment_id == Item.id)
            .join(Status, Status.id == RedressEquipment.tag_id)
            .join(Location, Location.id == RedressEquipment.location_id)
        )

        if asset_id is not None:
            query = query.where(RedressEquipment.asset_id == asset_id)

        query = query.order_by(RedressEquipment.completed_date.desc()).limit(100)

        result = await self.session.execute(query)
        return list(result.all())

    async def create_redress(self, data: dict) -> RedressEquipment:
        redress = RedressEquipment(**data)
        self.session.add(redress)
        await self.session.commit()
        await self.session.refresh(redress)
        return redress

    async def add_redress_step(self, redress_id: UUID, step_data: dict) -> RedressSteps:
        step = RedressSteps(redress_id=redress_id, **step_data)
        self.session.add(step)
        await self.session.commit()
        await self.session.refresh(step)
        return step

    async def complete_redress(self, redress_id: UUID) -> RedressEquipment:
        result = await self.session.execute(
            select(RedressEquipment)
            .where(RedressEquipment.id == redress_id)
        )
        redress = result.scalar_one()
        redress.status = 'completed'
        redress.completed_date = datetime.now()
        await self.session.commit()
        await self.session.refresh(redress)
        return redress
