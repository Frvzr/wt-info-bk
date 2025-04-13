from src.repository.service_equipment_repo import ServiceEquipmentRepository
from src.models import ServiceEquipment


class ServiceEquipmentService:
    def __init__(self, repository: ServiceEquipmentRepository):
        self.repository = repository

    async def get_all_service_equipments(self) -> list[ServiceEquipment]:
        return await self.repository.get_all()

    async def get_redress_by_id(self, id: str) -> list:
        return await self.repository.get_redress_by_id(id)
