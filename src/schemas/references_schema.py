from pydantic import BaseModel, ConfigDict, UUID4


class CategorySchema(BaseModel):
    id: UUID4
    name: str

    model_config = ConfigDict(from_attributes=True)
