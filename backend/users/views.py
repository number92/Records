from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from users.schemas import CreateUser
from users import crud
from core.db.db_helper import db_async_helper

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{id}/")
async def get_user(
    id: int,
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    user = await crud.get_user(user_id=id, async_session=session)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден"
    )


@router.post("/")
async def create_user(
    user: CreateUser,
    session: AsyncSession = Depends(db_async_helper.session_dependency),
):
    return await crud.create_user(user_in=user, async_session=session)
