"""edit services null-true

Revision ID: e2bc341affe2
Revises: 2aa867b692a1
Create Date: 2023-12-22 10:55:56.536213

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e2bc341affe2"
down_revision: Union[str, None] = "2aa867b692a1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "services", "specialist_id", existing_type=sa.INTEGER(), nullable=True
    )
    op.drop_column("services", "duration")
    op.alter_column(
        "specialists", "service_id", existing_type=sa.INTEGER(), nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "specialists", "service_id", existing_type=sa.INTEGER(), nullable=False
    )
    op.add_column(
        "services",
        sa.Column("duration", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.alter_column(
        "services", "specialist_id", existing_type=sa.INTEGER(), nullable=False
    )
    # ### end Alembic commands ###
