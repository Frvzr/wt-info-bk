"""added foreign keys for redress kit cinsist

Revision ID: 2925be905210
Revises: 2032e2e77320
Create Date: 2025-04-13 17:51:31.616276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2925be905210'
down_revision: Union[str, None] = '2032e2e77320'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'redress_kit_consist', 'redress_kit', ['redress_kit_id'], ['id'])
    op.create_foreign_key(None, 'redress_kit_consist', 'item', ['item_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'redress_kit_consist', type_='foreignkey')
    op.drop_constraint(None, 'redress_kit_consist', type_='foreignkey')
    # ### end Alembic commands ###
