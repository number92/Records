from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from specialists.models import Specialist
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


async def get_specialist_by_id_with_existing_speciality(
    specialist_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_async_helper.session_dependency),
) -> Specialist:
    stmt = (
        select(Specialist)
        .where(Specialist.id == specialist_id)
        .options(selectinload(Specialist.specializations))
        .order_by(Specialist.id)
    )
    spec_with_speciality = await session.scalar(stmt)
    if spec_with_speciality is not None:
        return spec_with_speciality
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Специалист не найден",
    )
