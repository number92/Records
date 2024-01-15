from typing import TYPE_CHECKING
from sqlalchemy import (
    ForeignKey,
    String,
    TIMESTAMP,
    Date,
    Time,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db.base import Base

if TYPE_CHECKING:
    from users.models import User
    from specialists.models import Specialist
    from services.models import Service


class Record(Base):
    """Запись"""

    __table_args__ = (
        UniqueConstraint(
            "date",
            "time",
            "specialist_id",
            name="idx_unique_datetime_specialist",
        ),
        UniqueConstraint(
            "date", "time", "user_id", name="idx_unique_datetime_user"
        ),
    )

    date: Mapped[TIMESTAMP] = mapped_column(Date)
    time: Mapped[TIMESTAMP] = mapped_column(Time)
    is_free: Mapped[bool | None] = mapped_column(default=True)
    note: Mapped[str | None] = mapped_column(String(256))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    specialist_id: Mapped[int] = mapped_column(ForeignKey("specialists.id"))
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))
    user: Mapped["User"] = relationship(back_populates="records")
    specialist: Mapped["Specialist"] = relationship(back_populates="records")
    service: Mapped["Service"] = relationship(back_populates="records")
