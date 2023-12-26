from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from services.schemas import GetService, CreateService
from services import crud
from core.db.db_helper import db_async_helper

router = APIRouter(prefix="/services", tags=["Service"])


@router.get("/{id}/")
async def get_service(
    id: int,
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    service = await crud.get_service(service_id=id, async_session=session)
    if service is not None:
        return service
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Услуга не найдена"
    )


@router.get("/")
async def get_list_services(
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    return crud.get_list_services(session)


@router.post("/")
async def create_service(
    service: CreateService,
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    return await crud.create_service(user_in=service, async_session=session)


@router.delete("/{id}/")
async def delete(
    id: int,
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    return crud.delete_service(session, service_id=id)
