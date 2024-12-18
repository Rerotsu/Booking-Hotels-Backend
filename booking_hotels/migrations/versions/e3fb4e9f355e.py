"""Добавление поля 'ФИО'в БД и подстроение эндпоинтов под это

Revision ID: e3fb4e9f355e
Revises: afe411bf70cb
Create Date: 2024-11-29 20:18:51.720571

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'e3fb4e9f355e'
down_revision: Union[str, None] = 'afe411bf70cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('hotels', 'services',
                existing_type=postgresql.JSON(astext_type=sa.Text()),
                type_=postgresql.JSONB(astext_type=sa.Text()),
                existing_nullable=True)
    op.alter_column('rooms', 'services',
                existing_type=postgresql.JSON(astext_type=sa.Text()),
                type_=postgresql.JSONB(astext_type=sa.Text()),
                existing_nullable=True)
    op.add_column('users', sa.Column('Full_name', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique') # type: ignore
    op.drop_column('users', 'Full_name')
    op.alter_column('rooms', 'services',
                existing_type=postgresql.JSONB(astext_type=sa.Text()),
                type_=postgresql.JSON(astext_type=sa.Text()),
                existing_nullable=True)
    op.alter_column('hotels', 'services',
                existing_type=postgresql.JSONB(astext_type=sa.Text()),
                type_=postgresql.JSON(astext_type=sa.Text()),
                existing_nullable=True)
    # ### end Alembic commands ###
