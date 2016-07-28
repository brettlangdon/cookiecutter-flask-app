"""Setup user and role tables

Revision ID: 70bd704dcb5c
Revises: None
Create Date: 2016-07-26 10:07:41.130632

"""

# revision identifiers, used by Alembic.
revision = '70bd704dcb5c'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


def upgrade():
    op.create_table(
        'role',
        sa.Column('id', UUID(), nullable=False),
        sa.Column('name', sa.String(length=80), nullable=True),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
    )
    op.create_table(
        'user',
        sa.Column('id', UUID(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('password', sa.String(length=255), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=True),
        sa.Column('confirmed_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
    )
    op.create_table(
        'user_role',
        sa.Column('user_id', UUID(), nullable=True),
        sa.Column('role_id', UUID(), nullable=True),
        sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    )


def downgrade():
    op.drop_table('user_role')
    op.drop_table('user')
    op.drop_table('role')
