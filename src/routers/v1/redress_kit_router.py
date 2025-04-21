from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import get_db
from src.repository.redres_kit_repo import RedressKitRepository
from src.services.redress_kit_service import RedressKitService
from src.schemas.redress_kit_schema import (RedressKitsSchema, RedressKitsWithItemsSchema,
                                            RedressKitsWithItemsSchemaById)

router = APIRouter(prefix="/api/v1/redress-kits", tags=["redress-kits"])


@router.get('/', response_model=list[RedressKitsSchema])
async def get_all_redress_kits(db: AsyncSession = Depends(get_db)):
    repository = RedressKitRepository(db)
    service = RedressKitService(repository)
    return await service.get_all_redress_kits()


@router.get('/consist/', response_model=list[RedressKitsWithItemsSchema])
async def get_all_redress_kits_with_items(db: AsyncSession = Depends(get_db)):
    repository = RedressKitRepository(db)
    service = RedressKitService(repository)
    return await service.get_all_redress_kits_with_items()


@router.get('/consist/{id}', response_model=list[RedressKitsWithItemsSchemaById])
async def get_redress_kits_with_items_by_name(id: str, db: AsyncSession = Depends(get_db)):
    repository = RedressKitRepository(db)
    service = RedressKitService(repository)
    return await service.get_redress_consist_by_id(id)
