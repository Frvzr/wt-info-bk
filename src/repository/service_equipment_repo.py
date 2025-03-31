from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models import ServiceEquipment, Asset, ServiceLevel, Location


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
