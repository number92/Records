from sqlalchemy import Result, select
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from specializations.models import Specialization
from specializations.schemas import (
    CreateSpecialization,
    GetSpecializationWithSpec,
)


async def get_specialization(
    async_session: AsyncSession, specialization_id: int
) -> Specialization:
    return await async_session.get(Specialization, specialization_id)


async def get_spcialization_with_specialist(
    specialization_id: int, async_session: AsyncSession
) -> GetSpecializationWithSpec:
    stmt = (
        select(Specialization)
        .where(Specialization.id == specialization_id)
        .options(selectinload(Specialization.specialists))
        .order_by(Specialization.id)
    )
    speciality_with_spec = await async_session.scalar(stmt)
    return speciality_with_spec


async def get_specializations(
    async_session: AsyncSession,
) -> list[Specialization]:
    stmt = select(Specialization).order_by(Specialization.id)
    result: Result = await async_session.execute(stmt)
    specializations = result.scalars().all()
    return specializations


async def create_specialization(
    async_session: AsyncSession, spec: CreateSpecialization
) -> Specialization:
    specialization = Specialization(**spec.model_dump())

    async_session.add(specialization)
    await async_session.commit()
    return specialization


async def delete_specialization(
    specialization: Specialization, async_session: AsyncSession
):
    await async_session.delete(specialization)
    await async_session.commit()
