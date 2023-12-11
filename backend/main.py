import os
import sys
from datetime import datetime

from db.orm import create_tables
from fastapi import FastAPI
from pydantic import BaseModel

# sys.path.insert(1, os.path.join(sys.path[0], '..'))

summary = 'API для записи, на прием'

app = FastAPI(
    title='Запись',
    summary=summary,
    )

create_tables()
# @app.get('/')
# def get_free_days():
#     return 10
