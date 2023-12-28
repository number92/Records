from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

from core.db.base import Base


specialist_specialization_association = Table(
    "specialist_specialization_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("specialist_id", ForeignKey("specialists.id"), nullable=False),
    Column(
        "specialization_id", ForeignKey("specializations.id"), nullable=False
    ),
    UniqueConstraint(
        "specialist_id",
        "specialization_id",
        name="idx_unique_specialist_specialist",
    ),
)
