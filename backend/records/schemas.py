from typing import Annotated
from annotated_types import MaxLen
from pydantic import BaseModel, ConfigDict, FutureDate, FutureDatetime


class SchemaRecord(BaseModel):
    title: Annotated[str, MaxLen(256)]
    date: FutureDate
    time: FutureDatetime.time
    user_id: int
    specialist_id: int


class CreateRecord(SchemaRecord):
    pass


class GetRecord(SchemaRecord):
    model_config = ConfigDict(from_attributes=True)
    id: int
