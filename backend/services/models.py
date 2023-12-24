from specialists.models import Specialist
from core.db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column


class Service(Base):
    """Услуга"""

    name: Mapped[str]
    specialist_id: Mapped[int | None] = mapped_column(
        ForeignKey("specialists.id")
    )
    specialists: Mapped[list["Specialist"]] = relationship(
        back_populates="service"
    )
