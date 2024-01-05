from pydantic import BaseModel, ConfigDict
from services.schemas import GetService


class SchemaSpecialization(BaseModel):
    name: str


class GetSpecialization(SchemaSpecialization):
    id: int
    model_config = ConfigDict(from_attributes=True)


class GetSpecializationWithServices(GetSpecialization):
    services: list[GetService]
    model_config = ConfigDict(from_attributes=True)


class CreateSpecialization(SchemaSpecialization):
    pass
