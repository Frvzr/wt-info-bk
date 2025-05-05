from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models import (RedressEquipment, Asset, ServiceLevel, Location, TemplateEquipment,
                        ChecklistTemplate, TemplateSteps, ChecklistSteps, RedressSteps)


class ServiceEquipmentRepository:
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

    async def get_redress_by_id(self, redress_id: uuid4) -> list:
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
