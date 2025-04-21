from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.references_repo import CategoryRepository
from src.services.references_service import CategoryService
from src.schemas.references_schema import CategorySchema
from src.db.database import get_db


router = APIRouter(prefix='/api/v1', tags=['reference'])


@router.get('/categories/', response_model=list[CategorySchema])
async def get_all_categories(db: AsyncSession = Depends(get_db)):
    repository = CategoryRepository(db)
    service = CategoryService(repository)
    return await service.get_all()
