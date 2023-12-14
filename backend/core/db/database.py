from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import (DeclarativeBase, Mapped, declared_attr,
                            mapped_column, sessionmaker)

from .config import settings


class Base(DeclarativeBase):
    __abstract__ = True
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
    # pool_size=5,
    # max_overflow=10
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
)

sync_session = sessionmaker(sync_engine)
async_session = async_sessionmaker(async_engine)
