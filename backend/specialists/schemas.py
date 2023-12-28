from typing import Annotated
from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict
from users.schemas import SchemaUser, Tg, Phone


str = Annotated[str, MinLen(2), MaxLen(256)]


class SchemaSpecialist(BaseModel):
    name: str
    middle_name: str
    last_name: str


class BaseId(BaseModel):
    id: int


class CreateSpecialist(SchemaUser, SchemaSpecialist):
    model_config = ConfigDict(coerce_numbers_to_str=True)


class GetSpecialist(SchemaSpecialist, BaseId):
    model_config = ConfigDict(from_attributes=True)


class GetSpecialistWithTg(Tg, SchemaSpecialist):
    model_config = ConfigDict(from_attributes=True)


class GetSpecialistWithPhone(Phone, SchemaSpecialist):
    model_config = ConfigDict(from_attributes=True)


class SpecialistUpdatePartial(CreateSpecialist):
    pass


class SpecialistUpdate(CreateSpecialist):
    pass
