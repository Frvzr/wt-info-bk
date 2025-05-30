from uuid import UUID
from fastapi import HTTPException

from ..repository.item_repo import ItemRepository
from src.models.item import Item
from src.schemas.item_schema import (
    ItemCreateSchema,
    ItemUpdateSchema,
    ItemSchema,
    ItemWithCategory,
    ItemDeleteResponse,
    ItemMarkDeleteResponse
)


class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    async def create_item(self, data: ItemCreateSchema) -> ItemSchema:
        existing = await self.repository.get_id_by_name(data.name)
        if existing:
            raise ValueError("Item already exists")
        item = await self.repository.create(data.model_dump())
        return ItemSchema.model_validate(item.__dict__)

    async def update_item(self, item_id: UUID, data: ItemUpdateSchema) -> ItemSchema:
        item = await self.repository.update(item_id, data.model_dump(exclude_unset=True))
        if not item:
            raise ValueError("Item not found")
        return ItemSchema.model_validate(item.__dict__)

    async def patch_item(self, item_id: UUID, data: ItemUpdateSchema) -> ItemSchema:
        item = await self.repository.patch(item_id, data.model_dump(exclude_unset=True))
        if not item:
            raise ValueError("Item not found")
        return ItemSchema.model_validate(item.__dict__)

    async def get_item(self, id: UUID):
        item = await self.repository.get_by_id(id)
        if not item:
            raise ValueError("Item not found")
        return ItemSchema.model_validate(item)

    async def get_item_with_info(self, id: UUID):
        item = await self.repository.get_item_with_info_by_id(id)
        if not item:
            raise ValueError("Item not found")
        return ItemWithCategory.model_validate(item)

    async def get_all_items(self) -> list[Item]:
        return await self.repository.get_all()

    async def get_items_with_category(self) -> list[Item]:
        return await self.repository.get_items_with_category()

    async def delete_item(self, item_id: UUID) -> ItemDeleteResponse:
        if not await self.repository.delete_item(item_id):
            raise HTTPException(
                status_code=404,
                detail="Item not found or already deleted"
            )
        return ItemDeleteResponse(
            status="deleted",
            deleted_id=str(item_id)
        )

    async def mark_delete(self, item_id: UUID) -> ItemMarkDeleteResponse:
        if not await self.repository.mark_delete(item_id):
            raise HTTPException(
                status_code=404,
                detail="Item not found or already deleted"
            )

        return ItemMarkDeleteResponse(
            id=item_id,
            status="soft_deleted",
            is_active=False
        )
