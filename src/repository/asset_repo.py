from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models import Asset, Equipment


class AssetRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self):
        query = await self.session.execute(
            select(Asset.serial_number,
                   Equipment.part_number)
            .select_from(Asset)
            .join(Equipment, isouter=True))

        result = query.all()
        return list(result)
