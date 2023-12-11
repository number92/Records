from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from .config import settings


class Base(DeclarativeBase):
    pass


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
    # pool_size=5,
    # max_overflow=10
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
)

session = sessionmaker(sync_engine)
async_session = async_sessionmaker(async_engine)
