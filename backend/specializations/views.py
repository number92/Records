from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from specializations.models import Specialization
from core.db.db_helper import db_async_helper
from specializations.schemas import (
    CreateSpecialization,
    GetSpecializationWithServices,
)
from specializations.dependencies import (
    get_specialization_by_id,
    get_specialization_by_id_with_existing_services,
)
from specializations import crud

router = APIRouter(prefix="/specializations", tags=["Специализация"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_specialization(
    specialization: CreateSpecialization,
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Создание специализации"""
    return await crud.create_specialization(
        spec=specialization, async_session=session
    )


@router.get("/")
async def get_list_specializations(
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Cписок специализаций"""
    return await crud.get_specializations(session)


@router.get("/{specialization_id}/")
async def get_specialization(
    specialization: Specialization = Depends(get_specialization_by_id),
):
    """Получение специализации по id"""
    return specialization


@router.delete(
    "/{specialization_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_specialization(
    specialization: Specialization = Depends(get_specialization_by_id),
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Удаление специализации"""
    await crud.delete_specialization(
        specialization=specialization, async_session=session
    )


@router.get(
    "/{specialization_id}/services/",
    status_code=status.HTTP_200_OK,
    response_model=GetSpecializationWithServices,
)
async def get_list_services_of_specializations(
    specialization=Depends(get_specialization_by_id_with_existing_services),
):
    """Список услуг специализации"""
    return specialization
