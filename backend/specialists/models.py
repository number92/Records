from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db.base import Base
from records.models import Record
from services.service_specialist_association import (
    specialist_service_association,
)
from specializations.specialist_specialization_association import (
    specialist_specialization_association,
)

if TYPE_CHECKING:
    from services.models import Service
    from specializations.models import Specialization


class Specialist(Base):
    """Cпециалист"""

    name: Mapped[str] = mapped_column(String(256))
    middle_name: Mapped[str] = mapped_column(String(256))
    last_name: Mapped[str] = mapped_column(String(256))
    telegram_id: Mapped[str]
    phone: Mapped[str]
    specializations: Mapped[list["Specialization"]] = relationship(
        secondary=specialist_specialization_association,
        back_populates="specialists",
    )
    services: Mapped[list["Service"]] = relationship(
        secondary=specialist_service_association, back_populates="specialists"
    )
    records: Mapped[list["Record"]] = relationship()
