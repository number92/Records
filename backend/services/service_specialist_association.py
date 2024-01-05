from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, UniqueConstraint

from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db.base import Base

if TYPE_CHECKING:
    from services.models import Service
    from specialists.models import Specialist


class SpecialistServiceAssociation(Base):
    """Связь услуга-специалист"""

    __tablename__ = "specialist_service_association"
    __table_args__ = (
        UniqueConstraint(
            "service_id", "specialist_id", name="idx_unique_service_specialist"
        ),
    )
    price: Mapped[int | None]
    description: Mapped[str | None]
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))
    specialist_id: Mapped[int] = mapped_column(ForeignKey("specialists.id"))
    service: Mapped["Service"] = relationship(
        back_populates="specialists_detail"
    )
    specialist: Mapped["Specialist"] = relationship(
        back_populates="services_detail"
    )
