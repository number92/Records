from services.models import Service
from services.schemas import CreateService, GetService
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


async def get_service(async_session: AsyncSession, service_id: int):
    return async_session.get(Service, service_id)


async def get_list_services(async_session: AsyncSession):
    stmt = select(Service).order_by(Service.id)
    result: Result = await async_session.execute(stmt)
    return list(result.scalars().all())


async def create_service(
    async_session: AsyncSession, service_in: CreateService
) -> Service | None:
    service = Service(**service_in.model_dump())
    async_session.add(service)
    await async_session.commit()
    return service


async def delete_service(async_session: AsyncSession, service_id: int):
    service = await async_session.get(Service, service_id)
    return async_session.delete(service)
