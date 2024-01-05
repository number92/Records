"""add attr

Revision ID: 0b110f6c7a0f
Revises: 20f1624cf4d5
Create Date: 2023-12-30 23:22:28.648986

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0b110f6c7a0f"
down_revision: Union[str, None] = "20f1624cf4d5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "services",
        "specialization_id",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.create_unique_constraint(None, "specializations", ["name"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "specializations", type_="unique")
    op.alter_column(
        "services",
        "specialization_id",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    # ### end Alembic commands ###
