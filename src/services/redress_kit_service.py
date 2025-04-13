from src.repository.redres_kit_repo import RedressKitRepository
from src.models import RedressKit, RedressKitConsist


class RedressKitService:
    def __init__(self, repository: RedressKitRepository):
        self.repository = repository

    async def get_all_redress_kits(self) -> list[RedressKit]:
        return await self.repository.get_all()

    async def get_all_redress_kits_with_items(self) -> list[RedressKitConsist]:
        return await self.repository.get_redress_kit_with_items()

    async def get_redress_consist_by_name(self, name: str) -> list:
        return await self.repository.get_redress_kit_consist_by_name(name)
