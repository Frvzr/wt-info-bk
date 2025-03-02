from pydantic import BaseModel, ConfigDict, UUID4

from .category import CategorySchema


class ItemSchema(BaseModel):
    id: UUID4
    name: str
    description: str | None
    category: UUID4 | None

    model_config = ConfigDict(from_attributes=True)


class ItemNameIdSchema(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)


class ItemWithCategory(BaseModel):
    id: UUID4
    item_name: str
    item_description: str | None
    category_name: str | None
    category_description: str | None

    class Config:
        from_attributes = True
