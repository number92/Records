from db.database import Base
from phonenumbers import PhoneNumber
from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table
from sqlalchemy.orm import Mapped, mapped_column

metadata = MetaData()


# class Specialization(Base):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(nullable=False)


specialization = Table(
    "specialization",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)

specialist = Table(
    "specialist",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "telegram_id",
        Integer,
    ),
    Column("name", String, nullable=False),
    Column("specialization", ForeignKey("specialization.id")),
)

users = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("telegram_id", Integer, nullable=False),
    Column("name", String, nullable=False),
    Column("middle_name", String),
    Column("last_name", String),
    Column("phone", Integer, nullable=False),
)
