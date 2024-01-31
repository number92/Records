from sqlalchemy import Result, select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from core.utils import get_or_create
from specializations.models import Specialization
from specializations.schemas import (
    CreateSpecialization,
    GetSpecializationWithServices,
)


async def get_specialization(
    async_session: AsyncSession, specialization_id: int
) -> Specialization:
    return await async_session.get(Specialization, specialization_id)


async def get_specialization_with_services(
    specialization_id: int, async_session: AsyncSession
) -> GetSpecializationWithServices:
    stmt = (
        select(Specialization)
        .where(Specialization.id == specialization_id)
        .options(selectinload(Specialization.services))
        .order_by(Specialization.id)
    )
    return await async_session.scalar(stmt)


async def get_specializations(
    async_session: AsyncSession,
) -> list[Specialization]:
    stmt = select(Specialization).order_by(Specialization.id)
    result: Result = await async_session.execute(stmt)
    return result.scalars().all()


async def create_specialization(
    async_session: AsyncSession, spec: CreateSpecialization
) -> Specialization:
    return await get_or_create(
        async_session=async_session,
        model=Specialization,
        **spec.model_dump(),
    )


async def delete_specialization(
    specialization: Specialization, async_session: AsyncSession
):
    await async_session.delete(specialization)
    await async_session.commit()
