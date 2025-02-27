from pydantic import BaseModel, ConfigDict, UUID4

from .category import CategorySchema


class ItemSchema(BaseModel):
    id: UUID4
    name: str
    description: str | None
    category: CategorySchema | None

    model_config = ConfigDict(from_attributes=True)


class ItemNameIdSchema(BaseModel):
    id: UUID4
    name: str

    model_config = ConfigDict(from_attributes=True)
