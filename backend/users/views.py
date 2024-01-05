from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from users.schemas import CreateUser
from users import crud
from users.dependencies import get_user_by_id
from core.db.db_helper import db_async_helper

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def get_list_users(
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    return await crud.get_list_users(async_session=session)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: CreateUser,
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    return await crud.create_user(user_in=user, async_session=session)


@router.get("/{user_id}/")
async def get_user(user: User = Depends(get_user_by_id)):
    return user
