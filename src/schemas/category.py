from pydantic import BaseModel, ConfigDict


class CategorySchema(BaseModel):
    name: str
    description: str | None

    model_config = ConfigDict(from_attributes=True)
