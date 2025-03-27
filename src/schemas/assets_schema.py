from pydantic import BaseModel, ConfigDict, UUID4


class AssetSchema(BaseModel):
    serial_number: str
    part_number: str

    model_config = ConfigDict(from_attributes=True)
