from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from users.schemas import CreateUser
from users import crud
from users.dependencies import get_user_by_id
from core.db.db_helper import db_async_helper

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{user_id}/")
async def get_user(user: User = Depends(get_user_by_id)):
    return user


@router.post("/")
async def create_user(
    user: CreateUser,
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    return await crud.create_user(user_in=user, async_session=session)
