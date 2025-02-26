from pydantic import BaseModel, ConfigDict

from .category import CategorySchema


class ItemSchema(BaseModel):
    name: str
    description: str | None
    category: CategorySchema | None

    model_config = ConfigDict(from_attributes=True)
