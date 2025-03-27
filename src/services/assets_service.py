from ..repository.asset_repo import AssetRepository
from src.models.asset import Asset


class AssetService:
    def __init__(self, repository: AssetRepository):
        self.repository = repository

    async def get_all_assets(self) -> list[Asset]:
        return await self.repository.get_all()
