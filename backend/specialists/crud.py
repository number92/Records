from fastapi import HTTPException, status
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from specialists.models import ProfileInfoSpecialist, Specialist
from specialists.schemas import (
    CreateProfileSpecialist,
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
    return spec


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


async def create_profile(
    async_session: AsyncSession,
    profile: CreateProfileSpecialist,
    specialist: Specialist,
) -> ProfileInfoSpecialist:
    spec = ProfileInfoSpecialist(
        specialist=specialist.id, **profile.model_dump()
    )
    stmt = select(ProfileInfoSpecialist).where(
        ProfileInfoSpecialist.specialist == specialist.id
    )
    check_duplicate = await async_session.execute(stmt)
    if check_duplicate.scalar():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Профиль специалиста уже существует",
        )
    async_session.add(spec)
    await async_session.commit()
    return spec
