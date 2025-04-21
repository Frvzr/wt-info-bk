from datetime import datetime
from pydantic import BaseModel, ConfigDict, UUID4


class RedressKitsSchema(BaseModel):
    redress_kit: str
    description: str | None = None
    actual_revision: str
    level: str

    model_config = ConfigDict(from_attributes=True)


class RedressKitsWithItemsSchema(BaseModel):
    redress_kit: str
    desc_redress_kit: str | None = None
    item: str
    desc_item: str | None = None
    quantity: float
    revision: str

    model_config = ConfigDict(from_attributes=True)


class RedressKitsWithItemsSchemaById(BaseModel):
    kit_id: UUID4
    kit_name: str
    component_id: UUID4
    component_name: str
    quantity: float
    revision: str

    model_config = ConfigDict(from_attributes=True)
