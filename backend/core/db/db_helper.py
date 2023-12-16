from .config import settings
from asyncio import current_task
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import (
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)


class DatabaseaAsyncHelper:
    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_asyncscoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory, scopefunc=current_task
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as sess:
            yield sess
            await sess.close()


db_async_helper = DatabaseaAsyncHelper(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
)


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
    # pool_size=5,
    # max_overflow=10
)


sync_session = sessionmaker(sync_engine)
