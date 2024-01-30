from typing import Any, List, Optional
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PositiveInt,
    model_validator,
)
from users.schemas import Tg, Phone
from datetime import time, datetime as dt


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


class ProfileSpecialist(BaseModel):
    start_work: time = Field(examples=["10:00"])
    end_work: time = Field(examples=["18:00"])
    busy_time: Optional[List[time]] = Field(
        examples=[["12:30", "16:30"]], default=[]
    )


class CreateProfileSpecialist(ProfileSpecialist):
    @model_validator(mode="after")
    def check_time_consistency(self) -> "ProfileSpecialist":
        dt_start_work = dt.combine(date=dt.today(), time=self.start_work)
        dt_end_work = dt.combine(date=dt.today(), time=self.end_work)
        if dt_start_work >= dt_end_work:
            raise ValueError(
                "Начало работы не должно быть позже его окончания"
            )
        return self


class ProfileUpdatePartial(ProfileSpecialist):
    start_work: time | None = Field(examples=["10:00"], default=None)
    end_work: time | None = Field(examples=["18:00"], default=None)


class ProfileUpdate(ProfileSpecialist):
    pass
