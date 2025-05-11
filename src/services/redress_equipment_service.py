from uuid import UUID
from typing import Optional
from datetime import datetime

from src.repository.asset_repo import AssetRepository
from src.repository.redress_equipment_repo import RedressEquipmentRepository
from src.schemas.redress_equipment_schema import (
    RedressEquipmentCreate, RedressStepCreate,
    ChecklistTemplate, RedressEquipment, RedressStep,
    RedressActivitySchema
)
from src.schemas.assets_schema import Asset


class RedressEquipmentService:
    def __init__(self, asset_repo: AssetRepository, redress_repo: RedressEquipmentRepository):
        self.asset_repo = asset_repo
        self.redress_repo = redress_repo

    async def search_asset(self, serial_number: str) -> Optional[Asset]:
        asset = await self.asset_repo.get_by_serial(serial_number)
        if not asset:
            return None
        return Asset.model_validate(asset)

    async def get_asset_history(self, asset_id: UUID) -> list[RedressEquipment]:
        history = await self.redress_repo.get_redress_history(asset_id)
        return history

    async def get_user_redresses(self, username: str) -> list[RedressEquipment]:
        redresses = await self.redress_repo.get_user_redresses(username)
        return [RedressEquipment.model_validate(item) for item in redresses]

    async def get_template(self, equipment_id: UUID, level_id: UUID) -> Optional[ChecklistTemplate]:
        template = await self.redress_repo.get_template_by_level(equipment_id, level_id)
        if not template:
            return None
        return ChecklistTemplate.model_validate(template)

    async def create_redress(self, data: RedressEquipmentCreate, username: str) -> RedressEquipment:
        redress_data = data.model_dump()
        redress_data['assigned_to'] = username
        redress = await self.redress_repo.create_redress(redress_data)
        return RedressEquipment.model_validate(redress)

    async def add_step_to_redress(self, redress_id: UUID, step_data: RedressStepCreate, username: str) -> RedressStep:
        step_data_dict = step_data.model_dump()
        step_data_dict['technician'] = username
        if step_data_dict['answer'] is not None:
            step_data_dict['completed_date'] = datetime.now()
        step = await self.redress_repo.add_redress_step(redress_id, step_data_dict)
        return RedressStep.model_validate(step)

    async def complete_redress(self, redress_id: UUID) -> RedressEquipment:
        redress = await self.redress_repo.complete_redress(redress_id)
        return RedressEquipment.model_validate(redress)
