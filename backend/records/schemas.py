from typing import Annotated
from datetime import time, datetime
from annotated_types import MaxLen
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    FutureDate,
    field_validator,
)

time_h_m = time

# date_d_m_y = Annotated[
#     FutureDate,
#     PlainSerializer(lambda x: date.strftime(x, "%d-%m-%Y")),
# ]


class SchemaRecord(BaseModel):
    date: FutureDate = Field(examples=["01/01/2023"])
    time: time_h_m = Field(examples=["14:30"])
    note: Annotated[str, MaxLen(256)] | None

    @field_validator("date", mode="before")
    def parse_date(cls, value):
        return datetime.strptime(value, "%d/%m/%Y").date()

    @field_validator("time", mode="before")
    def parse_time(cls, value):
        return datetime.strptime(value, "%H:%M").time()


class CreateRecord(SchemaRecord):
    pass


class GetRecord(SchemaRecord):
    model_config = ConfigDict(from_attributes=True)
    id: int
