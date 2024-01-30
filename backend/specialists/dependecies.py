from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from services.service_specialist_association import (
    SpecialistServiceAssociation,
)
from specialists.models import Specialist, ProfileInfoSpecialist
from specialists import crud
from core.db.db_helper import db_async_helper


async def get_specialist_by_id(
    specialist_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_async_helper.session_dependency),
) -> Specialist:
    spec = await crud.get_specialist(
        specialist_id=specialist_id, async_session=session
    )
    if spec is not None:
        return spec
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Специалист не найден",
    )


async def get_specialist_by_id_with_existing_services(
    specialist_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_async_helper.session_dependency),
) -> Specialist:
    stmt = (
        select(Specialist)
        .where(Specialist.id == specialist_id)
        .options(
            selectinload(Specialist.services_detail).joinedload(
                SpecialistServiceAssociation.service
            )
        )
        .order_by(Specialist.id)
    )
    spec_with_services = await session.scalar(stmt)
    if spec_with_services is not None:
        return spec_with_services
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Специалист не найден",
    )


async def get_profile_by_id(
    specialist_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_async_helper.session_dependency),
) -> ProfileInfoSpecialist:
    profile = await crud.get_profile(
        specialist_id=specialist_id, async_session=session
    )
    if profile is not None:
        return profile
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Профиль не найден",
    )
