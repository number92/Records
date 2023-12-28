from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db.base import Base
from specialists.models import Specialist
from specializations.specialist_specialization_association import (
    specialist_specialization_association,
)


class Specialization(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    specialists: Mapped[list["Specialist"]] = relationship(
        secondary=specialist_specialization_association,
        back_populates="specializations",
    )
