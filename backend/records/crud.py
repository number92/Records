from sqlalchemy import Result, select
from records.models import Record
from records.schemas import CreateRecord
from sqlalchemy.ext.asyncio import AsyncSession
from services.models import Service
from specialists.models import Specialist
from users.models import User


async def get_record(async_session: AsyncSession, record_id: int):
    return await async_session.get(Record, record_id)


async def create_record(
    async_session: AsyncSession,
    record_in: CreateRecord,
    user: User,
    specialist: Specialist,
    service: Service,
) -> Record:
    record = Record(**record_in.model_dump())
    record.user = user
    record.specialist = specialist
    record.service = service
    async_session.add(record)
    await async_session.commit()
    await async_session.refresh(record)
    return record


async def get_records_list(async_session: AsyncSession):
    stmt = select(Record).order_by(Record.id)
    result: Result = await async_session.execute(stmt)
    return result.scalars().all()


async def delete_record(record: Record, async_session: AsyncSession):
    await async_session.delete(record)
    await async_session.commit()
