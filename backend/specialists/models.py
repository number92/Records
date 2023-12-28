from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db.base import Base
from records.models import Record
from services.service_specialist_association import (
    specialist_service_association,
)

if TYPE_CHECKING:
    from services.models import Service
    from specializations.models import Specialization


class Specialist(Base):
    """Cпециалист"""

    name: Mapped[str] = mapped_column(String(256))
    middle_name: Mapped[str] = mapped_column(String(256))
    last_name: Mapped[str] = mapped_column(String(256))
    telegram_id: Mapped[int]
    phone: Mapped[str]
    specialization_id: Mapped[int] = mapped_column(
        ForeignKey("specializations.id")
    )
    specialization: Mapped["Specialization"] = relationship(
        back_populates="specialists"
    )
    services: Mapped[list["Service"]] = relationship(
        secondary=specialist_service_association, back_populates="specialists"
    )
    records: Mapped[list["Record"]] = relationship()
