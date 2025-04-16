from pydantic import BaseModel, ConfigDict, UUID4


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

    model_config = ConfigDict(from_attributes=True)

class ItemWithCategory(BaseModel):
    id: UUID4
    item: str
    item_description: str | None = None
    category: str | None = None
    group: str | None = None
    source: str | None = None
    operation: str | None = None
    department: str | None = None

    model_config = ConfigDict(from_attributes=True)
