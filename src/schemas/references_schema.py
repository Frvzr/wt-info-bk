from pydantic import BaseModel, ConfigDict, UUID4


class CategorySchema(BaseModel):
    id: UUID4
    name: str

    model_config = ConfigDict(from_attributes=True)


class SourceSchema(BaseModel):
    id: UUID4
    name: str

    model_config = ConfigDict(from_attributes=True)


class GroupSchema(BaseModel):
    id: UUID4
    name: str

    model_config = ConfigDict(from_attributes=True)


class OperationSchema(BaseModel):
    id: UUID4
    name: str

    model_config = ConfigDict(from_attributes=True)


class DepartmentSchema(BaseModel):
    id: UUID4
    name: str

    model_config = ConfigDict(from_attributes=True)