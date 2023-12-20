from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db.base import Base

from specialists.models import Specialist


class Specialization(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    specialists: Mapped[list["Specialist"]] = relationship(
        back_populates="specialization"
    )
