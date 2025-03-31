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
