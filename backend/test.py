import asyncio

from db.database import async_engine, sync_engine
from sqlalchemy import text


async def get_123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text('SELECT 1,2,3 union select 4,5,6'))
        print(res.first())


asyncio.run(get_123())
