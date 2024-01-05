from sqlalchemy import Result, select
from users.models import User
from users.schemas import CreateUser
from sqlalchemy.ext.asyncio import AsyncSession


async def get_user(async_session: AsyncSession, user_id: int):
    return await async_session.get(User, user_id)


async def get_list_users(async_session: AsyncSession):
    stmt = select(User).order_by(User.id)
    result: Result = await async_session.execute(stmt)
    return result.scalars().all()


async def create_user(
    async_session: AsyncSession, user_in: CreateUser
) -> User | None:
    user = User(**user_in.model_dump())

    async_session.add(user)
    await async_session.commit()
    return user
