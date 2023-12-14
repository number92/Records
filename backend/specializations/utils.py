from __future__ import annotations

from typing import Union

from phonenumbers import NumberParseException
from phonenumbers import PhoneNumber as _PhoneNumber
from phonenumbers import (PhoneNumberFormat, format_number, is_possible_number,
                          parse)
from pydantic import BaseModel


class PhoneNumber(_PhoneNumber):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Union[str, PhoneNumber]) -> PhoneNumber:
        if isinstance(v, PhoneNumber):
            return v
        try:
            number = parse(v, None)
        except NumberParseException as ex:
            raise ValueError(f"Invalid phone number: {v}") from ex
        if not is_possible_number(number):
            raise ValueError(f"Invalid phone number: {v}")
        return number

    def json_encode(self) -> str:
        return format_number(self, PhoneNumberFormat.E164)


class MyModel(BaseModel):
    phone_number: PhoneNumber


test_number = PhoneNumber("9811397677")

print(test_number)
