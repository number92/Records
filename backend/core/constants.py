from datetime import time

REGION: str = "RU"
LEN_T_ID: int = 10  # Длина Телеграм id

# Формирование расписания
DAYS: int = 14  # На две недели вперед
WORK_TIME: dict[str, time] = {
    "start_work": time(10, 0),
    "end_work": time(18, 0),
}
BUSY_TIME: dict[str, time] = [
    {"start": time(11, 30), "end": time(12, 0)},
    {"start": time(13, 00), "end": time(14, 0)},
    {"start": time(16, 30), "end": time(17, 0)},
]
