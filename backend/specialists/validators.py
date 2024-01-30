from datetime import time, datetime as dt


def validate_consistency_time(start_work: time, end_work: time):
    dt_start_work = dt.combine(date=dt.today(), time=start_work)
    dt_end_work = dt.combine(date=dt.today(), time=end_work)
    if dt_start_work >= dt_end_work:
        return False
    return True
