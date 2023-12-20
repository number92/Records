from sqlalchemy import ForeignKey, String, TIMESTAMP, Date, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db.base import Base
from users.models import User


class Record(Base):
    """Записи"""

    title: Mapped[str] = mapped_column(String(256))
    date: Mapped[TIMESTAMP] = mapped_column(Date)
    time: Mapped[TIMESTAMP] = mapped_column(Time)
    is_free: Mapped[bool] = mapped_column(default=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    specialist_id: Mapped[int] = mapped_column(ForeignKey("specialists.id"))
    user: Mapped["User"] = relationship()
