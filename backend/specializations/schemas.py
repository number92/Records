from pydantic import BaseModel, ConfigDict


class SchemaSpecialization(BaseModel):
    name: str


class GetSpecialization(SchemaSpecialization):
    model_config = ConfigDict(from_attributes=True)
    id: int


class CreateSpecialization(SchemaSpecialization):
    pass
