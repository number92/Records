from pydantic import BaseModel, ConfigDict, PositiveInt
from users.schemas import Tg, Phone


class SchemaSpecialist(BaseModel):
    name: str
    middle_name: str
    last_name: str


class BaseId(BaseModel):
    id: int


class BaseService(BaseId):
    name: str
    duration: PositiveInt


class CreateSpecialist(Tg, Phone, SchemaSpecialist):
    model_config = ConfigDict(coerce_numbers_to_str=True)


class GetSpecialist(SchemaSpecialist, BaseId):
    model_config = ConfigDict(from_attributes=True)


class GetSpecialistWithTg(Tg, SchemaSpecialist):
    model_config = ConfigDict(from_attributes=True)


class GetSpecialistWithPhone(Phone, SchemaSpecialist):
    model_config = ConfigDict(from_attributes=True)


class ServiceDetail(BaseModel):
    price: int | None = None
    description: str | None = None
    service: BaseService


class SpecWithServices(GetSpecialist):
    services_detail: list[ServiceDetail]
    model_config = ConfigDict(from_attributes=True)


class SpecialistUpdatePartial(Tg, Phone, SchemaSpecialist):
    name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None
    phone: str | None = None
    telegram_id: str | None = None


class SpecialistUpdate(CreateSpecialist):
    pass
