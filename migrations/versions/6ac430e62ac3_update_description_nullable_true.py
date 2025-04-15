"""update description, nullable True

Revision ID: 6ac430e62ac3
Revises: 3a80bf624aaf
Create Date: 2025-04-15 07:48:57.002435

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ac430e62ac3'
down_revision: Union[str, None] = '3a80bf624aaf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'description',
               existing_type=sa.VARCHAR(length=512),
               nullable=True)
    op.drop_constraint('departments_description_key', 'departments', type_='unique')
    op.create_unique_constraint(None, 'departments', ['id'])
    op.create_unique_constraint(None, 'groups', ['id'])
    op.alter_column('operations', 'description',
               existing_type=sa.VARCHAR(length=512),
               nullable=True)
    op.drop_constraint('operations_description_key', 'operations', type_='unique')
    op.create_unique_constraint(None, 'operations', ['id'])
    op.alter_column('sources', 'description',
               existing_type=sa.VARCHAR(length=512),
               nullable=True)
    op.drop_constraint('sources_description_key', 'sources', type_='unique')
    op.create_unique_constraint(None, 'sources', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'sources', type_='unique')
    op.create_unique_constraint('sources_description_key', 'sources', ['description'])
    op.alter_column('sources', 'description',
               existing_type=sa.VARCHAR(length=512),
               nullable=False)
    op.drop_constraint(None, 'operations', type_='unique')
    op.create_unique_constraint('operations_description_key', 'operations', ['description'])
    op.alter_column('operations', 'description',
               existing_type=sa.VARCHAR(length=512),
               nullable=False)
    op.drop_constraint(None, 'groups', type_='unique')
    op.drop_constraint(None, 'departments', type_='unique')
    op.create_unique_constraint('departments_description_key', 'departments', ['description'])
    op.alter_column('departments', 'description',
               existing_type=sa.VARCHAR(length=512),
               nullable=False)
    # ### end Alembic commands ###
