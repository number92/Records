from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from services.dependencies import get_service_by_id
from services.models import Service
from specialists.dependecies import get_specialist_by_id
from specialists.models import Specialist
from users.dependencies import get_user_by_id
from users.models import User
from core.db.db_helper import db_async_helper
from records import crud
from records.schemas import CreateRecord, GetRecordWithAllRelations
from records.models import Record
from records.dependencies import (
    get_record_by_id,
    get_record_with_all_relations,
)

router = APIRouter(prefix="/records", tags=["Records"])


@router.get("/")
async def get_records_list(
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Получение списка записей"""
    return await crud.get_records_list(session)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_record(
    record_in: CreateRecord,
    user: User = Depends(get_user_by_id),
    specialist: Specialist = Depends(get_specialist_by_id),
    service: Service = Depends(get_service_by_id),
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Добавление записи"""
    return await crud.create_record(
        record_in=record_in,
        async_session=session,
        user=user,
        specialist=specialist,
        service=service,
    )


@router.get("/{id}/", response_model=GetRecordWithAllRelations)
async def get_record(
    record: Record = Depends(get_record_with_all_relations),
):
    """Получение записи по id"""
    return record


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_record(
    record: Record = Depends(get_record_by_id),
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Удаление записи"""
    await crud.delete_record(record=record, async_session=session)
