from pydantic import BaseModel, ConfigDict, UUID4


class AssetSchema(BaseModel):
    id: UUID4
    serial_number: str
    part_number: str
    description: str

    model_config = ConfigDict(from_attributes=True)
