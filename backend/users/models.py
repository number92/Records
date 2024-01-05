from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db.base import Base

from records.models import Record


class User(Base):
    """Пользователь"""

    name: Mapped[str] = mapped_column(String(256))
    telegram_id: Mapped[str]
    phone: Mapped[str]
    records: Mapped[list["Record"]] = relationship(back_populates="user")
