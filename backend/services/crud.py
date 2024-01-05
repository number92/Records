from fastapi import HTTPException, status
from specialists.models import Specialist
from services.models import Service
from services.schemas import (
    CreateService,
    GetServiceSpecialistDetail,
    ServiceWithSpecialists,
)
from services.service_specialist_association import (
    SpecialistServiceAssociation,
)
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


async def get_service(async_session: AsyncSession, service_id: int):
    return await async_session.get(Service, service_id)


async def get_list_services(async_session: AsyncSession):
    stmt = select(Service).order_by(Service.id)
    result: Result = await async_session.execute(stmt)
    return result.scalars().all()


async def get_service_with_specialists(
    service_id: int, async_session: AsyncSession
) -> ServiceWithSpecialists:
    stmt = (
        select(Service)
        .where(Service.id == service_id)
        .options(
            selectinload(Service.specialists_detail).joinedload(
                SpecialistServiceAssociation.specialist
            )
        )
        .order_by(Service.id)
    )
    return await async_session.scalar(stmt)


async def create_service(
    async_session: AsyncSession, service_in: CreateService
) -> Service:
    service = Service(**service_in.model_dump())
    async_session.add(service)
    await async_session.commit()
    return service


async def delete_service(
    service: Service, async_session: AsyncSession
) -> None:
    await async_session.delete(service)
    await async_session.commit()


async def add_specialist_to_service(
    specialist: Specialist,
    service_with_spec: Service,
    async_session: AsyncSession,
    service_detail: GetServiceSpecialistDetail,
):
    for assoc in service_with_spec.specialists_detail:
        if specialist == assoc.specialist:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=(
                    f"У специалиста уже есть услуга: {service_with_spec.name}"
                ),
            )
    service_detail = service_detail.model_dump()
    service_with_spec.specialists_detail.append(
        SpecialistServiceAssociation(
            price=service_detail["price"],
            description=service_detail["description"],
            specialist=specialist,
            specialist_id=specialist.id,
        )
    )
    await async_session.commit()
    return await async_session.get(Service, service_with_spec.id)


async def delete_service_to_specialist(
    specialist: Specialist,
    service: Service,
    async_session: AsyncSession,
):
    for assoc in service.specialists_detail:
        if specialist == assoc.specialist:
            await async_session.delete(assoc)
            await async_session.commit()
            return

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Услуга отсутствует у этого специалиста",
    )
