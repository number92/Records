from models.models import metadata
from sqlalchemy import insert

from .database import async_engine, sync_engine


def create_tables():
    metadata.drop_all(sync_engine)
    metadata.create_all(sync_engine)