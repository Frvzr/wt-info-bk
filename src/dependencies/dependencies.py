from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.repository.asset_repo import AssetRepository
from src.repository.redress_equipment_repo import RedressEquipmentRepository
from src.services.redress_equipment_service import RedressEquipmentService
from src.db.database import get_db


async def get_asset_repository(session: AsyncSession = Depends(get_db)):
    return AssetRepository(session)


async def get_redress_repository(session: AsyncSession = Depends(get_db)):
    return RedressEquipmentRepository(session)


async def get_redress_service(
    asset_repo: AssetRepository = Depends(get_asset_repository),
    redress_repo: RedressEquipmentRepository = Depends(get_redress_repository)
):
    return RedressEquipmentService(asset_repo, redress_repo)
