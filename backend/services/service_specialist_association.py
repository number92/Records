from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

from core.db.base import Base

specialist_service_association = Table(
    "specialist_service_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("service_id", ForeignKey("services.id"), nullable=False),
    Column("specialist_id", ForeignKey("specialists.id"), nullable=False),
    UniqueConstraint(
        "service_id", "specialist_id", name="idx_unique_service_specialist"
    ),
)
