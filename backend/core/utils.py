# import os
# import sys
import re

import regex
import phonenumbers
from datetime import date as d, datetime as dt, timedelta as td
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import INTERVAL
from sqlalchemy.sql.functions import concat


# sys.path.insert(0, os.path.join(os.getcwd()))
# sys.path.insert(0, os.path.join(os.getcwd(), "backend"))


from services.models import Service
from specialists.models import Specialist
from records.models import Record
from core import constants

# from core.db.db_helper import db_async_helper, async_session


def normalize_num(number: str):
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
                    number_obj = phonenumbers.parse(number, constants.REGION)
                    if phonenumbers.is_possible_number(number_obj):
                        return phonenumbers.format_number(
                            number_obj, phonenumbers.PhoneNumberFormat.E164
                        )
        except phonenumbers.NumberParseException as e:
            errormessage = " number {}. Error: {}".format(number, e.message)
            raise UserWarning(errormessage)
    raise ValueError("Неверный формат номера")


def check_not_busy_time(starttime: dt, duration: int):
    """
    Проверка: не занято ли время?
    На вход время записи и длительность услуги
    на выход {is_free: bool}
    """
    endtime = starttime + td(minutes=duration)
    res = {"is_free": True}
    for busy_time in constants.BUSY_TIME:
        start_busy_time = dt.combine(starttime.date(), busy_time["start"])
        end_busy_time = dt.combine(starttime.date(), busy_time["end"])
        if starttime == start_busy_time:
            res["is_free"] = False
        if start_busy_time < endtime <= end_busy_time:
            res["is_free"] = False
        if start_busy_time <= starttime < end_busy_time:
            res["is_free"] = False
        if starttime <= start_busy_time and end_busy_time <= endtime:
            res["is_free"] = False
        if start_busy_time <= starttime and endtime <= end_busy_time:
            res["is_free"] = False
    return res


def time_during_the_day(date: dt, duration: int):
    """
    Создание промежутков времени в одном дне,
    На вход принимается дата и продожительность услуги
    """
    res = []
    start_time: dt = dt.combine(date, constants.WORK_TIME["start_work"])
    end_time: dt = dt.combine(date, constants.WORK_TIME["end_work"])
    first_time = check_not_busy_time(start_time, duration)
    if first_time["is_free"]:
        res.append(start_time)
    while start_time < end_time:
        start_time = start_time + td(minutes=duration)
        status = check_not_busy_time(start_time, duration)
        if status["is_free"]:
            res.append(start_time)
    return res


# day1 = dt(2024, 1, 30)
# print(time_during_the_day(date=day1, duration=30))


async def scheduling(
    session: AsyncSession, specialist: Specialist, service: Service
):
    """Формирование расписания"""
    datetime_list = []
    duration = service.duration
    print(duration)
    today = d.today()
    for i in range(0, constants.DAYS - 1):
        date = today + td(days=i)
        datetime_list.append(time_during_the_day(date=date, duration=duration))
    return datetime_list


async def get_list_records_in_next_two_weeks(
    specialist_id: int,
    session: AsyncSession,
):
    stmt = (
        select(Record)
        .where(Record.specialist_id == specialist_id)
        .filter(
            Record.date
            <= (
                func.now()
                + func.cast(concat(constants.DAYS, " DAYS"), INTERVAL)
            )
        )
    )
    result: Result = await session.execute(statement=stmt)
    return result.scalars().all()
    # async with session() as session:
    #     # result: Result = await session.execute(statement=stmt)
    #     print(await session.scalars(statement=stmt))
    #     await session.close()


# asyncio.run(
#     get_list_records_in_next_two_weeks(
#                                    specialist_id=1,
#                                    session=async_session
#     )
# )
