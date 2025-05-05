from uuid import UUID

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.item_repo import ItemRepository
from src.services.item_service import ItemService
from src.schemas.item_schema import (
    ItemSchema,
    ItemWithCategory,
    ItemUpdateSchema,
    ItemCreateSchema,
    ItemDeleteResponse,
    ItemMarkDeleteResponse
)
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


@router.get("/{id}", response_model=ItemSchema)
async def get_item(id: str, db: AsyncSession = Depends(get_db)):
    try:
        repository = ItemRepository(db)
        service = ItemService(repository)
        return await service.get_item(id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get('/info/{id}', response_model=ItemWithCategory)
async def get_item_with_info(id: str, db: AsyncSession = Depends(get_db)):
    repository = ItemRepository(db)
    service = ItemService(repository)
    return await service.get_item_with_info(id)


@router.put("/{id}", response_model=ItemUpdateSchema)
async def update_item(
        id: str,
        data: ItemUpdateSchema,
        db: AsyncSession = Depends(get_db)
):
    try:
        repository = ItemRepository(db)
        service = ItemService(repository)
        return await service.update_item(id, data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.patch("/{id}", response_model=ItemSchema)
async def partial_update_item(
        id: str,
        data: ItemUpdateSchema,
        db: AsyncSession = Depends(get_db)
):
    try:
        repository = ItemRepository(db)
        service = ItemService(repository)
        return await service.patch_item(id, data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{id}", response_model=ItemDeleteResponse)
async def delete_item(
    id: UUID,
    db: AsyncSession = Depends(get_db)
):
    repository = ItemRepository(db)
    service = ItemService(repository)
    return await service.delete_item(id)


@router.patch("/{item_id}/mark-delete", response_model=ItemMarkDeleteResponse)
async def mark_delete(
    item_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    item_repo = ItemRepository(db)
    item_service = ItemService(item_repo)
    return await item_service.mark_delete(item_id)
