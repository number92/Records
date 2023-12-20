from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from core.db.base import Base
from records.models import Record


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
    records: Mapped[list["Record"]] = relationship(
        "Record", back_populates="specialist"
    )
