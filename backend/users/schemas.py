import re
from typing import Annotated
from annotated_types import MaxLen, MinLen, Len
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
)
from core.utils import normalize_num
from core.constants import LEN_T_ID


class SchemaUser(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(256)]
    telegram_id: int | Annotated[str, Len(LEN_T_ID)]
    phone: str = Field(
        pattern=r"\d+", min_length=10, max_length=12, examples=["+79812223355"]
    )

    @field_validator("telegram_id")
    @classmethod
    def telegram_id_to_str(cls, v) -> str:
        if isinstance(v, int) and len(str(v)) != LEN_T_ID:
            raise ValueError("telegram_id должен состоять из 10 символов")
        return v

    @field_validator("phone")
    @classmethod
    def check_phone(cls, number) -> str:
        if re.search(r"\d+", number):
            return normalize_num(number)
        raise ValueError("Неверный формат номера")


class CreateUser(SchemaUser):
    model_config = ConfigDict(coerce_numbers_to_str=True)


class GetUser(SchemaUser):
    model_config = ConfigDict(from_attributes=True)
    id: int
