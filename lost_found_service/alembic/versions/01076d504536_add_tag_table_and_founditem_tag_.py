"""add Tag table and founditem_tag association

Revision ID: 01076d504536
Revises: 25d7d3b5f3e5
Create Date: 2025-03-13 15:22:02.908312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01076d504536'
down_revision: Union[str, None] = '25d7d3b5f3e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('founditem_tag',
    sa.Column('found_item_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['found_item_id'], ['found_items.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('found_item_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('founditem_tag')
    # ### end Alembic commands ###
