from ..repository.item_repo import ItemRepository
from src.models.item import Item
from src.schemas.item_schema import ItemCreateSchema, ItemUpdateSchema, ItemSchema


class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    async def create_item(self, data: ItemCreateSchema) -> ItemSchema:
        existing = await self.repository.get_id_by_name(data.name)
        if existing:
            raise ValueError("Item already exists")
        item = await self.repository.create(data.model_dump())
        return ItemSchema.model_validate(item.__dict__)

    async def update_item(self, item_id: int, data: ItemUpdateSchema) -> ItemSchema:
        item = await self.repository.update(item_id, data.model_dump(exclude_unset=True))
        if not item:
            raise ValueError("Item not found")
        return ItemSchema.model_validate(item)

    async def patch_item(self, item_id: int, data: ItemUpdateSchema) -> ItemSchema:
        return await self.update_item(item_id, data)

    async def get_item(self, item_id: int) -> ItemSchema:
        item = await self.repository.get_by_id(item_id)
        if not item:
            raise ValueError("Item not found")
        return ItemSchema.model_validate(item)

    async def get_all_items(self) -> list[Item]:
        return await self.repository.get_all()

    async def get_items_with_category(self) -> list[Item]:
        return await self.repository.get_items_with_category()
