from typing import TYPE_CHECKING, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db.base import Base

if TYPE_CHECKING:
    from records.models import Record


class User(Base):
    """Пользователь"""

    name: Mapped[str] = mapped_column(String(256))
    telegram_id: Mapped[int]
    phone: Mapped[str]
    records: Mapped[Optional[list["Record"]]] = relationship(
        "Record", back_populates="user"
    )
