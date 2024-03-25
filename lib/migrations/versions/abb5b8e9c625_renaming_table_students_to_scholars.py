"""renaming table students to scholars

Revision ID: abb5b8e9c625
Revises: 791279dd0760
Create Date: 2024-03-25 17:00:44.114143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abb5b8e9c625'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
