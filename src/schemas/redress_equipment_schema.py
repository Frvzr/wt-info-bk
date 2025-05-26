from datetime import datetime
from pydantic import BaseModel, ConfigDict, UUID4, Field


class RedressActivitySchema(BaseModel):
    id: UUID4
    serial_number: str
    part_number: str
    level: str
    tag: str
    completed_to: str
    completed_date: datetime
    top_tool: str
    #tool_time: str
    location: str
    #last_action: str


class RedressUserHistorySchema(BaseModel):
    id: UUID4
    serial_number: str
    part_number: str
    level: str
    created_at: datetime
    completed_date: datetime
    status: str


class RedressEquipmentSchema(BaseModel):
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


class RedressStepBase(BaseModel):
    step_id: UUID4
    answer: dict | None = None
    comment: str | None = None


class RedressStep(RedressStepBase):
    id: UUID4
    technician: str | None = None
    completed_date: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class RedressStepCreate(RedressStepBase):
    pass


class RedressEquipmentBase(BaseModel):
    asset_id: UUID4
    template_id: UUID4 | None = None
    tag: UUID4


class RedressEquipmentCreate(RedressEquipmentBase):
    assigned_to: str = Field(..., max_length=32)
    location_id: UUID4


class RedressEquipment(RedressEquipmentBase):
    id: UUID4
    status: str
    completed_date: datetime | None = None
    #steps: list[RedressStep] = []

    model_config = ConfigDict(from_attributes=True)


class TemplateStepBase(BaseModel):
    name: str = Field(..., max_length=32)
    description: str = Field(..., max_length=300)
    fields: dict | None = None


class TemplateStep(TemplateStepBase):
    id: UUID4
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class ChecklistTemplateBase(BaseModel):
    name: str = Field(..., max_length=32)
    description: str = Field(..., max_length=256)
    level_id: UUID4
    version: str = Field(..., max_length=32)


class ChecklistTemplate(ChecklistTemplateBase):
    id: UUID4
    is_active: bool
    steps: list[TemplateStep] = []

    model_config = ConfigDict(from_attributes=True)
