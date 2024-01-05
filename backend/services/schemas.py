from pydantic import BaseModel, ConfigDict, PositiveInt

from specialists.schemas import GetSpecialist


class SchemaService(BaseModel):
    name: str
    duration: PositiveInt


class CreateService(SchemaService):
    specialization_id: int | None


class GetService(SchemaService):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ServiceWithSpecialists(GetService):
    specialists: list[GetSpecialist]


class GetServiceSpecialistDetail(BaseModel):
    price: int | None
    description: str | None


class ResponseDetail(GetServiceSpecialistDetail):
    specialist: GetSpecialist


class ResponseServiceSpec(GetService):
    specialists_detail: list[ResponseDetail]
    model_config = ConfigDict(from_attributes=True)
