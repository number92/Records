import re
import regex
import phonenumbers
from core.constants import REGION


def normalize_num(number):
    if re.search(r"\d+", number):
        number = regex.sub(r"[^0-9\+]", "", number.lower(), regex.V0)
        try:
            if not number.startswith(("+", "8")) and len(number) == 10:
                number = "+7" + number
                number_obj = phonenumbers.parse(number)
                if phonenumbers.is_possible_number(number_obj):
                    return phonenumbers.format_number(
                        number_obj, phonenumbers.PhoneNumberFormat.E164
                    )
            if number.startswith("+"):
                number_obj = phonenumbers.parse(number)
                if phonenumbers.is_possible_number(number_obj):
                    return phonenumbers.format_number(
                        number_obj, phonenumbers.PhoneNumberFormat.E164
                    )
            else:
                if len(number) >= 11 and number.startswith("8"):
                    number = number[1:]
                    number_obj = phonenumbers.parse(number, REGION)
                    if phonenumbers.is_possible_number(number_obj):
                        return phonenumbers.format_number(
                            number_obj, phonenumbers.PhoneNumberFormat.E164
                        )
        except phonenumbers.NumberParseException as e:
            errormessage = " number {}. Error: {}".format(number, e.message)
            raise UserWarning(errormessage)
    raise ValueError("Неверный формат номера")
