from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.item import ItemRepository
from src.services.item import ItemService
from src.schemas.item import ItemSchema, ItemWithCategory
from src.db.database import get_db


router = APIRouter()


@router.get('/items/', response_model=list[ItemSchema])
async def get_all_items(db: AsyncSession = Depends(get_db)):
    repository = ItemRepository(db)
    service = ItemService(repository)
    return await service.get_all_items()


@router.get('/itemscat/', response_model=list[ItemWithCategory])
async def get_item_with_description(db: AsyncSession = Depends(get_db)):
    repository = ItemRepository(db)
    service = ItemService(repository)
    return await service.get_items_with_category()
