from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from services.dependencies import get_service_by_id
from services.models import Service
from specialists.dependecies import get_specialist_by_id
from specialists.models import Specialist
from users.dependencies import get_user_by_id
from users.models import User
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
    return await crud.get_records_list(session)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_record(
    record_in: CreateRecord,
    user: User = Depends(get_user_by_id),
    specialist: Specialist = Depends(get_specialist_by_id),
    service: Service = Depends(get_service_by_id),
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    return await crud.create_record(
        record_in=record_in,
        async_session=session,
        user=user,
        specialist=specialist,
        service=service,
    )
