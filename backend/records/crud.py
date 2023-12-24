from records.models import Record
from records.schemas import CreateRecord
from sqlalchemy.ext.asyncio import AsyncSession


async def get_record(async_session: AsyncSession, record_id: int):
    return await async_session.get(Record, record_id)


async def create_record(
    async_session: AsyncSession, record_in: CreateRecord
) -> Record | None:
    record = Record(**record_in.model_dump())

    async_session.add(record)
    await async_session.commit()
    return record


async def get_records_list(async_session: AsyncSession):
    pass
