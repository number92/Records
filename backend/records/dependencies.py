from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.db.db_helper import db_async_helper
from records.models import Record
from records import crud


async def get_record_by_id(
    record_id: int | Annotated[int, Path],
    session: AsyncSession = Depends(db_async_helper.session_dependency),
) -> Record:
    record = await crud.get_record(record_id=record_id, async_session=session)
    if record is not None:
        return record
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Запись не найдена",
    )
