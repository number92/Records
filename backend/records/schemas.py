from typing import Annotated
from datetime import datetime, date, time
from annotated_types import MaxLen
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
)
from services.schemas import SchemaService
from specialists.schemas import GetSpecialistWithPhone
from users.schemas import SchemaUserPhone

time_h_m = time
date_ge = date


class SchemaRecord(BaseModel):
    date: date
    time: str
    note: Annotated[str, MaxLen(256)] | None

    @field_validator("time", mode="before")
    def time_to_str(cls, value):
        date_to = f"{value.hour}:{value.minute}"
        return date_to


class CreateRecord(BaseModel):
    date: date_ge = Field(ge=date.today(), examples=["01/01/2023"])
    time: time_h_m = Field(examples=["14:30"])
    note: Annotated[str, MaxLen(256)] | None
    is_free: bool = False

    @field_validator("date", mode="before")
    def parse_date(cls, value):
        return datetime.strptime(value, "%d/%m/%Y").date()

    @field_validator("time", mode="before")
    def parse_time(cls, value):
        return datetime.strptime(value, "%H:%M").time()


class GetRecord(SchemaRecord):
    model_config = ConfigDict(from_attributes=True)
    id: int


class GetRecordWithAllRelations(SchemaRecord):
    user: SchemaUserPhone
    specialist: GetSpecialistWithPhone
    service: SchemaService

    model_config = ConfigDict()
