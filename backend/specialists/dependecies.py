from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
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
        detail="Специализация не найдена",
    )
