from specialists.models import Specialist
from core.db.base import Base
from sqlalchemy.orm import Mapped, relationship
from services.service_specialist_association import (
    specialist_service_association,
)


class Service(Base):
    """Услуга"""

    name: Mapped[str]
    duration: Mapped[int]
    specialists: Mapped[list["Specialist"]] = relationship(
        secondary=specialist_service_association, back_populates="services"
    )
