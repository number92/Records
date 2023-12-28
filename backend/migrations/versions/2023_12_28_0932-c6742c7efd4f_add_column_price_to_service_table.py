"""add column price to service table

Revision ID: c6742c7efd4f
Revises: 461eb8f1798d
Create Date: 2023-12-28 09:32:39.735554

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c6742c7efd4f"
down_revision: Union[str, None] = "461eb8f1798d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("services", sa.Column("price", sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("services", "price")
    # ### end Alembic commands ###
