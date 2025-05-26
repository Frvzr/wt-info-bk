from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from uuid import UUID
from src.schemas.redress_equipment_schema import (
    RedressEquipmentCreate, RedressEquipment,
    RedressStepCreate, RedressStep, RedressActivitySchema,
    RedressUserHistorySchema
)
from src.schemas.assets_schema import Asset
from src.services.redress_equipment_service import RedressEquipmentService
from src.dependencies.dependencies import get_redress_service

router = APIRouter(prefix="/redress", tags=["redress"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/search/{serial_number}", response_model=Asset)
async def search_asset(
    serial_number: str,
    service: RedressEquipmentService = Depends(get_redress_service)
):
    asset = await service.search_asset(serial_number)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset


@router.get("/history/{asset_id}", response_model=list[RedressActivitySchema])
async def get_asset_history(
    asset_id: UUID,
    service: RedressEquipmentService = Depends(get_redress_service)
):
    return await service.get_asset_history(asset_id)

@router.get("/history/", response_model=list[RedressActivitySchema])
async def get_asset_history(
    service: RedressEquipmentService = Depends(get_redress_service)
):
    return await service.get_full_asset_history()


@router.get("/user-redresses", response_model=list[RedressUserHistorySchema])
async def get_user_redresses(
    #token: str = Depends(oauth2_scheme),
    service: RedressEquipmentService = Depends(get_redress_service)
):
    username = "RU152"  # Заглушка
    return await service.get_user_redresses(username)


@router.post("/create", response_model=RedressEquipment)
async def create_redress(
    data: RedressEquipmentCreate,
    #token: str = Depends(oauth2_scheme),
    service: RedressEquipmentService = Depends(get_redress_service)
):
    username = "RU152"  # Заглушка
    return await service.create_redress(data, username)


@router.post("/{redress_id}/steps", response_model=RedressStep)
async def add_redress_step(
    redress_id: UUID,
    step_data: RedressStepCreate,
    #token: str = Depends(oauth2_scheme),
    service: RedressEquipmentService = Depends(get_redress_service)
):
    username = "RU152"
    return await service.add_step_to_redress(redress_id, step_data, username)


@router.post("/{redress_id}/complete", response_model=RedressEquipment)
async def complete_redress(
    redress_id: UUID,
    #token: str = Depends(oauth2_scheme),
    service: RedressEquipmentService = Depends(get_redress_service)
):
    return await service.complete_redress(redress_id)