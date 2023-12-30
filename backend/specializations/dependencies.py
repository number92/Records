from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from specializations.models import Specialization
from specializations import crud
from core.db.db_helper import db_async_helper


async def get_specialization_by_id(
    specialization_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_async_helper.session_dependency),
) -> Specialization:
    specialization = await crud.get_specialization(
        specialization_id=specialization_id, async_session=session
    )
    if specialization is not None:
        return specialization
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Специализация не найдена",
    )


async def get_specialization_by_id_with_existing_specialists(
    specialization_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    specialization = await crud.get_spcialization_with_specialist(
        specialization_id=specialization_id, async_session=session
    )
    if specialization is not None:
        return specialization
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Специализация не найдена",
    )
