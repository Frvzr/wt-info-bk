from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models import Asset


class AssetRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    # async def get_all(self):
    #     query = await self.session.execute(
    #         select(
    #             Asset.id,
    #             Asset.serial_number,
    #             Equipment.part_number,
    #             Equipment.description)
    #         .select_from(Asset)
    #         .join(Equipment, isouter=True))
    #
    #     result = query.all()
    #     return list(result)

    async def get_by_serial(self, serial_number: str) -> Asset | None:
        result = await self.session.execute(
            select(Asset.id,
                   Asset.serial_number,
                   Asset.equipment_id,
                   Asset.is_active,
                   Asset.status)
            .where(Asset.serial_number == serial_number)
        )
        return result.mappings().first()
