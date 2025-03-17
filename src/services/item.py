from sqlalchemy.util import await_only

from ..repository.item import ItemRepository
from ..schemas.item import ItemSchema


class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    async def get_all_items(self):
        return await self.repository.get_all()
