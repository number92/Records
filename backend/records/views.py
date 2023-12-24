from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.db.db_helper import db_async_helper
from records import crud
from records.schemas import CreateRecord

router = APIRouter(prefix="/records", tags=["Records"])


@router.get("/{id}/")
async def get_record(
    id: int,
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    record = await crud.get_record(record_id=id, async_session=session)
    if record is not None:
        return record
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найден"
    )


@router.get("/")
async def get_records_list(
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    return await crud.get_record_list(session)


@router.post("/")
async def create_record(
    record: CreateRecord,
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    return await crud.create_record(user_in=record, async_session=session)
