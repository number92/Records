from fastapi import HTTPException, status
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from specializations.models import Specialization
from specialists.models import Specialist
from specialists.schemas import (
    CreateSpecialist,
    SpecialistUpdatePartial,
    SpecialistUpdate,
)


async def create_specialist(
    async_session: AsyncSession, specialist: CreateSpecialist
) -> Specialist:
    spec = Specialist(**specialist.model_dump())
    async_session.add(spec)
    await async_session.commit()
    return Specialist


async def get_specialist(
    async_session: AsyncSession, specialist_id: int
) -> Specialist:
    return await async_session.get(Specialist, specialist_id)


async def get_specialists(
    async_session: AsyncSession,
) -> list[Specialist]:
    stmt = select(Specialist).order_by(Specialist.id)
    result: Result = await async_session.execute(stmt)
    specialists = result.scalars().all()
    return specialists


async def update_specialist(
    async_session: AsyncSession,
    specialist: Specialist,
    specialist_update: SpecialistUpdate | SpecialistUpdatePartial,
    partial: bool = False,
) -> Specialist:
    for name, value in specialist_update.model_dump(
        exclude_unset=partial
    ).items():
        setattr(specialist, name, value)
    await async_session.commit()
    return specialist


async def delete_specialist(
    specialist: Specialist, async_session: AsyncSession
):
    await async_session.delete(specialist)
    await async_session.commit()


async def add_speciality_to_specialist(
    specialist: Specialist,
    specialization: Specialization,
    async_session: AsyncSession,
):
    if specialization in specialist.specializations:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Специализация уже добавлена",
        )
    specialist.specializations.append(specialization)
    await async_session.commit()
    return specialist.specializations


async def delete_speciality_to_specialist(
    specialist: Specialist,
    specialization: Specialization,
    async_session: AsyncSession,
):
    if specialization not in specialist.specializations:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Специализация отсутствует у этого специалиста",
        )
    specialist.specializations.remove(specialization)
    await async_session.commit()
