from datetime import datetime
from pydantic import BaseModel, ConfigDict, UUID4


class ServiceEquipmentSchema(BaseModel):
    id: UUID4
    serial_number: str
    level: str
    location: str
    alias: str
    completed_date: datetime | None = None
    is_completed: bool

    model_config = ConfigDict(from_attributes=True)


class RedressSchema(BaseModel):
    name: str
    answer: str | None = None
    technician: str | None = None
    completed_date: str | None = None

    model_config = ConfigDict(from_attributes=True)


class RedressByIDSchema(BaseModel):
    step: str
    description: str
    answer: str | None = None
    technician: str | None = None
    completed_date: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
