from pydantic import BaseModel, ConfigDict, UUID4, field_validator
from typing import Optional


class ItemSchema(BaseModel):
    id: UUID4
    name: str
    description: str | None = None
    category_id: UUID4 | None = None
    group_id: UUID4 | None = None
    source_id: UUID4 | None = None
    operation_id: UUID4 | None = None
    department_id: UUID4 | None = None

    model_config = ConfigDict(from_attributes=True)


class ItemCreateSchema(BaseModel):
    name: str
    description: str | None = None
    category_id: UUID4 | None = None
    group_id: UUID4 | None = None
    source_id: UUID4 | None = None
    operation_id: UUID4 | None = None
    department_id: UUID4 | None = None

    model_config = ConfigDict(from_attributes=True)


class ItemUpdateSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    category_id: UUID4 | None = None
    group_id: UUID4 | None = None
    source_id: UUID4 | None = None
    operation_id: UUID4 | None = None
    department_id: UUID4 | None = None

    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v: str) -> Optional[str]:
        return None if v == "" else v

    model_config = ConfigDict(from_attributes=True)


class ItemWithCategory(BaseModel):
    id: UUID4
    name: str
    description: str | None = None
    category: str | None = None
    group: str | None = None
    source: str | None = None
    operation: str | None = None
    department: str | None = None

    model_config = ConfigDict(from_attributes=True)


class ItemDeleteResponse(BaseModel):
    status: str
    deleted_id: UUID4


class ItemMarkDeleteResponse(BaseModel):
    id: UUID4
    status: str
    is_active: bool
