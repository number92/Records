from typing import TYPE_CHECKING

from core.db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from services.service_specialist_association import (
    SpecialistServiceAssociation,
)

if TYPE_CHECKING:
    from specializations.models import Specialization


class Service(Base):
    """Услуга"""

    name: Mapped[str]
    duration: Mapped[int]

    specialization_id: Mapped[int] = mapped_column(
        ForeignKey("specializations.id", ondelete="SET NULL"), nullable=True
    )
    specialization: Mapped["Specialization"] = relationship(
        back_populates="services"
    )

    specialists_detail: Mapped[
        list["SpecialistServiceAssociation"]
    ] = relationship(back_populates="service")
