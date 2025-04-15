from pydantic import BaseModel, ConfigDict, UUID4


class ItemSchema(BaseModel):
    id: UUID4
    name: str
    description: str | None
    category_id: UUID4 | None

    model_config = ConfigDict(from_attributes=True)


class ItemNameIdSchema(BaseModel):
    name: str

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

    class Config:
        from_attributes = True
