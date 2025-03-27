
from ..repository.item import ItemRepository
from src.models.item import Item


class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    async def get_all_items(self) -> list[Item]:
        return await self.repository.get_all()

    async def get_items_with_category(self) -> list[Item]:
        return await self.repository.get_items_with_category()
