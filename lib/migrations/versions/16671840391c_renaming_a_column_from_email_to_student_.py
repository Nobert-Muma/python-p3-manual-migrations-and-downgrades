"""Renaming a column from email to student_email

Revision ID: 16671840391c
Revises: 2298c6c2cbc5
Create Date: 2024-09-14 20:44:05.101696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16671840391c'
down_revision = '2298c6c2cbc5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name='student_email')


def downgrade() -> None:
    op.alter_column('students', 'student_email', new_column_name='email')
