from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from users import crud
from core.db.db_helper import db_async_helper


async def get_user_by_id(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_async_helper.session_dependency),
) -> User:
    user = await crud.get_user(user_id=user_id, async_session=session)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден"
    )
