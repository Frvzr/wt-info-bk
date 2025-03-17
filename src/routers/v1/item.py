from fastapi import APIRouter, Depends
from src.repository.item import ItemRepository
from src.services.item import ItemService
from src.schemas.item import ItemSchema
from src.db.database import get_db

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get('/items/', response_model=list[ItemSchema])
async def get_all_items(db: AsyncSession = Depends(get_db)):
    repository = ItemRepository(db)
    service = ItemService(repository)
    return await service.get_all_items()
