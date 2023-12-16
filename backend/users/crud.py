from users.models import User
from users.schemas import CreateUser
from sqlalchemy.ext.asyncio import AsyncSession


async def get_user(async_session: AsyncSession, user_id: int):
    return async_session.get(User, user_id)


async def create_user(
    async_session: AsyncSession, user_in: CreateUser
) -> User | None:
    user = User(**user_in.model_dump())
    print(user)
    async_session.add(user)
    await async_session.commit()
    return user
