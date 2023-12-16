from typing import Annotated, Optional
from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict, validator

from core.utils import normalize_num


class ShemaUser(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(256)]
    telegram_id: int
    phone: Annotated[str, MinLen(10), MaxLen(12)]

    @validator("phone")
    def check_phone(cls, number):
        return normalize_num(number)


class CreateUser(ShemaUser):
    pass


class GetUser(ShemaUser):
    model_config = ConfigDict(from_attributes=True)
    id: int
