from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.asset_repo import AssetRepository
from src.services.assets_service import AssetService
from src.schemas.assets_schema import AssetListSchema
from src.db.database import get_db

router = APIRouter()


@router.get('/assets/', response_model=list[AssetListSchema])
async def get_all_assets(db: AsyncSession = Depends(get_db)):
    repository = AssetRepository(db)
    service = AssetService(repository)
    return await service.get_all_assets()
