from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.service_equipment_repo import ServiceEquipmentRepository
from src.services.service_equipment_service import ServiceEquipmentService
from src.schemas.service_equipment_schema import ServiceEquipmentSchema, RedressByIDSchema
from src.db.database import get_db

router = APIRouter()


@router.get('/activity/', response_model=list[ServiceEquipmentSchema])
async def get_all_activity(db: AsyncSession = Depends(get_db)):
    repository = ServiceEquipmentRepository(db)
    service = ServiceEquipmentService(repository)
    return await service.get_all_service_equipments()


@router.get('/activity/{id}', response_model=list[RedressByIDSchema])
async def get_redress_by_id(id: str, db: AsyncSession = Depends(get_db)):
    repository = ServiceEquipmentRepository(db)
    service = ServiceEquipmentService(repository)
    return await service.get_redress_by_id(id)
