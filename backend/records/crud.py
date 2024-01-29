from fastapi import HTTPException, status
from sqlalchemy import Result, select
from records.models import Record
from records.schemas import CreateRecord
from sqlalchemy.ext.asyncio import AsyncSession
from services.models import Service
from specialists.models import Specialist
from users.models import User
from services.service_specialist_association import (
    SpecialistServiceAssociation as assoc,
)


async def get_record(async_session: AsyncSession, record_id: int):
    return await async_session.get(Record, record_id)


async def create_record(
    async_session: AsyncSession,
    record_in: CreateRecord,
    user: User,
    specialist: Specialist,
    service: Service,
) -> Record:
    exist_service_specialist_relation = select(assoc).where(
        assoc.service_id == service.id, assoc.specialist_id == specialist.id
    )
    check_service = await async_session.execute(
        exist_service_specialist_relation
    )
    if not check_service.scalar():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Услуга отсутствует у этого специалиста",
        )
    stmt = select(Record).where(
        Record.time == record_in.time
        and Record.date == record_in.date
        and Record.specialist_id == specialist.id
    )
    check_duplicate = await async_session.execute(stmt)
    if check_duplicate.scalar():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Запись к специалисту на эту дату и время уже существует",
        )
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
