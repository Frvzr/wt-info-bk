"""added is_active for items

Revision ID: 870d876fc86b
Revises: 2564137c66f6
Create Date: 2025-05-02 13:11:58.199730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '870d876fc86b'
down_revision: Union[str, None] = '2564137c66f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('groups', 'description')
    op.add_column('item', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'is_active')
    op.add_column('groups', sa.Column('description', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
