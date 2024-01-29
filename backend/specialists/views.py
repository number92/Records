from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.utils import get_list_records_in_next_two_weeks
from specialists.models import Specialist
from core.db.db_helper import db_async_helper
from specialists.schemas import (
    CreateProfileSpecialist,
    CreateSpecialist,
    GetSpecialist,
    SpecialistUpdate,
    SpecialistUpdatePartial,
    SpecWithServices,
)
from specialists.dependecies import (
    get_specialist_by_id,
    get_specialist_by_id_with_existing_services,
)
from specialists import crud

router = APIRouter(prefix="/specialists", tags=["Specialists"])


@router.get("/", response_model=list[GetSpecialist])
async def get_list_specialits(
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Cписок специалистов"""
    return await crud.get_specialists(session)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_specialist(
    specialist: CreateSpecialist,
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Создание специалиста"""
    return await crud.create_specialist(
        specialist=specialist, async_session=session
    )


@router.get("/{specialist_id}/")
async def get_specialist(
    specialist: Specialist = Depends(get_specialist_by_id),
):
    """Получение специалиста по id"""
    return specialist


@router.get(
    "/{specialist_id}/services/",
    status_code=status.HTTP_200_OK,
    response_model=SpecWithServices,
)
async def get_list_services_of_specialist(
    specialist: Specialist = Depends(
        get_specialist_by_id_with_existing_services
    ),
):
    """Список услуг специалиста"""
    return specialist


@router.put("/{specialist_id}/", status_code=status.HTTP_200_OK)
async def update_specialist(
    specialist_update: SpecialistUpdate,
    specialist: Specialist = Depends(get_specialist_by_id),
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Обновление специалиста"""
    return await crud.update_specialist(
        specialist=specialist,
        specialist_update=specialist_update,
        async_session=session,
        partial=True,
    )


@router.patch("/{specialist_id}/", status_code=status.HTTP_200_OK)
async def update_specialist_partial(
    specialist_update: SpecialistUpdatePartial,
    specialist: Specialist = Depends(get_specialist_by_id),
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Частичное обновление специалиста"""
    return await crud.update_specialist(
        specialist=specialist,
        specialist_update=specialist_update,
        async_session=session,
        partial=True,
    )


@router.delete(
    "/{specialist_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_specialist(
    specialist: Specialist = Depends(get_specialist_by_id),
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Удаление специалиста"""
    await crud.delete_specialist(specialist=specialist, async_session=session)


@router.post("/{specialist_id}/profile")
async def create_profile(
    profile: CreateProfileSpecialist,
    specialist: Specialist = Depends(get_specialist_by_id),
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Создание  профиля специалиста"""
    return await crud.create_profile(
        specialist=specialist, async_session=session, profile=profile
    )


@router.get(
    "/{specialist_id}/schedule",
)
async def get_schedule(
    specialist_id: int,
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    return await get_list_records_in_next_two_weeks(
        session=session, specialist_id=specialist_id
    )
