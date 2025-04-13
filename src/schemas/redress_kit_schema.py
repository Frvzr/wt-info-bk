from datetime import datetime
from pydantic import BaseModel, ConfigDict, UUID4


class RedressKitsSchema(BaseModel):
    redress_kit: str
    description: str | None = None
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


class RedressKitsWithItemsSchemaByName(BaseModel):
    item: str
    desc_item: str
    quantity: float
    revision: str

    model_config = ConfigDict(from_attributes=True)
