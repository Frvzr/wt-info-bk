from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import get_db
from src.repository.redres_kit_repo import RedressKitRepository
from src.services.redress_kit_service import RedressKitService
from src.schemas.redress_kit_schema import RedressKitsSchema, RedressKitsWithItemsSchema

router = APIRouter()

@router.get('/redress_kits/', response_model=RedressKitsSchema)
async def get_all_redress_kits(db: AsyncSession = Depends(get_db)):
    repository = RedressKitRepository(db)
    service = RedressKitService(repository)
    return await service.get_all_redress_kits()

@router.get('/redress_kits_items/', response_model=RedressKitsWithItemsSchema)
async def get_all_redress_kits_with_items(db:AsyncSession = Depends(get_db)):
    repository = RedressKitRepository(db)
    service = RedressKitService(repository)
    return await service.get_all_redress_kits_with_items()
