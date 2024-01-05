from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from services.models import Service
from services import crud
from services.schemas import ServiceWithSpecialists
from core.db.db_helper import db_async_helper


async def get_service_by_id(
    service_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_async_helper.session_dependency),
) -> Service:
    service = await crud.get_service(
        service_id=service_id, async_session=session
    )
    if service is not None:
        return service
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Услуга не найдена",
    )


async def get_service_by_id_with_existing_specialists(
    service_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_async_helper.session_dependency),
) -> ServiceWithSpecialists:
    service_with_spec = await crud.get_service_with_specialists(
        service_id=service_id, async_session=session
    )
    if service_with_spec is not None:
        return service_with_spec
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Услуга не найдена",
    )
