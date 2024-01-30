from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from specialists.dependecies import get_specialist_by_id
from specialists.models import Specialist
from services.dependencies import (
    get_service_by_id,
    get_service_by_id_with_existing_specialists,
)
from services.models import Service
from services.schemas import (
    CreateService,
    ResponseServiceSpec,
    GetServiceSpecialistDetail,
)
from services import crud
from core.db.db_helper import db_async_helper

router = APIRouter(prefix="/services", tags=["Услуга"])


@router.get("/")
async def get_list_services(
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    return await crud.get_list_services(session)


@router.post("/")
async def create_service(
    service: CreateService,
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    return await crud.create_service(service_in=service, async_session=session)


@router.get(
    "/{service_id}/",
    response_model=ResponseServiceSpec,
)
async def get_service(
    service: Service = Depends(get_service_by_id_with_existing_specialists),
):
    """Получение услуги по id"""
    return service


@router.delete(
    "/{service_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_service(
    service: Service = Depends(get_service_by_id),
    session: AsyncSession = Depends(db_async_helper.session_dependency),
) -> None:
    """Удаление услуги по id"""
    await crud.delete_service(async_session=session, service=service)


@router.post(
    "/{service_id}/specialists/{specialist_id}/",
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseServiceSpec,
)
async def add_specialist_to_service(
    service_detail: GetServiceSpecialistDetail,
    specialist: Specialist = Depends(get_specialist_by_id),
    service: Service = Depends(get_service_by_id_with_existing_specialists),
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Добавление специалиста к услуге"""
    return await crud.add_specialist_to_service(
        specialist=specialist,
        service_with_spec=service,
        async_session=session,
        service_detail=service_detail,
    )


@router.delete(
    "/{service_id}/services/{specialist_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_specialist_to_service(
    specialist: Specialist = Depends(get_specialist_by_id),
    service: Service = Depends(get_service_by_id_with_existing_specialists),
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    """Удаление услуги у специалиста"""
    await crud.delete_service_to_specialist(
        async_session=session,
        specialist=specialist,
        service=service,
    )
