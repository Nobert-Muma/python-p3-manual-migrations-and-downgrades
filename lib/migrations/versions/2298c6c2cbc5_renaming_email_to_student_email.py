"""Renaming email to student_email

Revision ID: 2298c6c2cbc5
Revises: 5cd1a2721ad9
Create Date: 2024-09-14 20:33:25.333456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2298c6c2cbc5'
down_revision = '5cd1a2721ad9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name='student_email')


def downgrade() -> None:
    op.alter_column('students', 'student_email', new_column_name='email')
