from pydantic import BaseModel, ConfigDict, UUID4, Field


class AssetBase(BaseModel):
    serial_number: str = Field(..., max_length=32)


class AssetSchema(AssetBase):
    id: UUID4
    part_number: str
    description: str | None = None
    status: str


class Asset(AssetBase):
    id: UUID4
    equipment_id: UUID4
    is_active: bool
    status: UUID4

    model_config = ConfigDict(from_attributes=True)
