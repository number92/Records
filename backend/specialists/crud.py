from fastapi import HTTPException, status
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from specialists import validators
from specialists.models import ProfileInfoSpecialist as Profile, Specialist
from specialists.schemas import (
    CreateProfileSpecialist,
    CreateSpecialist,
    ProfileUpdate,
    ProfileUpdatePartial,
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
) -> Profile:
    spec = Profile(specialist=specialist.id, **profile.model_dump())
    stmt = select(Profile).where(Profile.specialist == specialist.id)
    check_duplicate = await async_session.execute(stmt)
    if check_duplicate.scalar():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Профиль специалиста уже существует",
        )
    async_session.add(spec)
    await async_session.commit()
    return spec


async def get_profile(
    async_session: AsyncSession,
    specialist_id: int,
) -> Profile | None:
    stmt = select(Profile).where(Profile.specialist == specialist_id)
    profile: Result = await async_session.execute(stmt)
    return profile.scalar_one_or_none()


async def update_profile(
    async_session: AsyncSession,
    profile: Profile,
    profile_update: ProfileUpdatePartial | ProfileUpdate,
    partial: bool = False,
) -> Profile:
    for name, value in profile_update.model_dump().items():
        if not value:
            value = getattr(profile, name)
        setattr(profile, name, value)
    if validators.validate_consistency_time(
        profile.start_work,
        profile.end_work,
    ):
        await async_session.commit()
        return profile
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Начало работы не должно быть позднее ее окончания",
        )
