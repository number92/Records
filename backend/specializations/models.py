from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db.base import Base

if TYPE_CHECKING:
    from services.models import Service


class Specialization(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    services: Mapped[list["Service"]] = relationship(
        passive_deletes=True, back_populates="specialization"
    )
