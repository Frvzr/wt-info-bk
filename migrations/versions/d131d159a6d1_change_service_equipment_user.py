"""change Service equipment, User

Revision ID: d131d159a6d1
Revises: db4cb4226df2
Create Date: 2025-03-31 22:33:06.635901

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd131d159a6d1'
down_revision: Union[str, None] = 'db4cb4226df2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('service_equipment_template_id_fkey', 'service_equipment', type_='foreignkey')
    op.create_foreign_key(None, 'service_equipment', 'template_equipment', ['template_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'service_equipment', type_='foreignkey')
    op.create_foreign_key('service_equipment_template_id_fkey', 'service_equipment', 'checklist_templates', ['template_id'], ['id'])
    # ### end Alembic commands ###
