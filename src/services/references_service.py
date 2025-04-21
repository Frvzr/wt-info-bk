from src.repository.references_repo import CategoryRepository
from src.models import Category


class CategoryService:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    async def get_all(self) -> list[Category]:
        return await self.repository.get_all()
