from pydantic import BaseModel, ConfigDict
from specialists.schemas import GetSpecialist


class SchemaSpecialization(BaseModel):
    name: str


class GetSpecialization(SchemaSpecialization):
    id: int
    model_config = ConfigDict(from_attributes=True)


class GetSpecializationWithSpec(GetSpecialization):
    specialists: list[GetSpecialist]
    model_config = ConfigDict(from_attributes=True)


class CreateSpecialization(SchemaSpecialization):
    pass
