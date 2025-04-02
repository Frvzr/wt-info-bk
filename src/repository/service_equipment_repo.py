from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models import (ServiceEquipment, Asset, ServiceLevel, Location, TemplateEquipment,
                        ChecklistTemplate,TemplateSteps, ChecklistSteps, ServiceSteps)


class ServiceEquipmentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[ServiceEquipment]:
        query = await self.session.execute(
            select(ServiceEquipment.id,
                   Asset.serial_number,
                   ServiceLevel.name.label('level'),
                   Location.name.label('location'),
                   ServiceEquipment.completed_technician.label('alias'),
                   ServiceEquipment.completed_date,
                   ServiceEquipment.is_completed)
            .select_from(ServiceEquipment)
            .join(Asset, isouter=True)
            .join(ServiceLevel)
            .join(Location)
        )
        result = query.all()
        return list(result)

    async def get_redress_by_id(self, redress_id: uuid4) -> list:
        query = await self.session.execute(
            select(
                   ChecklistSteps.name,
                   ServiceSteps.answer,
                   ServiceSteps.technician,
                   ServiceSteps.completed_date
                   )
            .select_from(ServiceSteps)
            .join(ChecklistSteps)
            .where(ServiceEquipment.id == redress_id)
        )
        result = query.all()
        return list(result)
