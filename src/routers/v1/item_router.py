from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.item_repo import ItemRepository
from src.services.item_service import ItemService
from src.schemas.item_schema import (
    ItemSchema,
    ItemWithCategory,
    ItemUpdateSchema,
    ItemCreateSchema)
from src.db.database import get_db


router = APIRouter(prefix="/api/v1/items", tags=["items"])


@router.post("/", response_model=ItemCreateSchema, status_code=status.HTTP_201_CREATED)
async def create_item(
        data: ItemCreateSchema,
        db: AsyncSession = Depends(get_db)
):
    try:
        repository = ItemRepository(db)
        service = ItemService(repository)
        return await service.create_item(data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get('/', response_model=list[ItemSchema])
async def get_all_items(db: AsyncSession = Depends(get_db)):
    repository = ItemRepository(db)
    service = ItemService(repository)
    return await service.get_all_items()


@router.get('/full/', response_model=list[ItemWithCategory])
async def get_item_with_description(db: AsyncSession = Depends(get_db)):
    repository = ItemRepository(db)
    service = ItemService(repository)
    return await service.get_items_with_category()
