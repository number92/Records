from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db.base import Base
from records.models import Record
from services.service_specialist_association import (
    SpecialistServiceAssociation,
)


class Specialist(Base):
    """Cпециалист"""

    name: Mapped[str] = mapped_column(String(256))
    middle_name: Mapped[str] = mapped_column(String(256))
    last_name: Mapped[str] = mapped_column(String(256))
    telegram_id: Mapped[str]
    phone: Mapped[str]
    services_detail: Mapped[
        list["SpecialistServiceAssociation"]
    ] = relationship(back_populates="specialist", cascade="all")
    records: Mapped[list["Record"]] = relationship(back_populates="specialist")
