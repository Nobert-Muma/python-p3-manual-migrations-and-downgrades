"""Renaming students to scholars

Revision ID: 5cd1a2721ad9
Revises: 791279dd0760
Create Date: 2024-09-14 20:24:43.791323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cd1a2721ad9'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
