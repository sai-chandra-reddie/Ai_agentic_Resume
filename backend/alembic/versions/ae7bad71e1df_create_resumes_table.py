"""create_resumes_table

Revision ID: ae7bad71e1df
Revises: 
Create Date: 2026-09-19 13:40:45.022709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB


# revision identifiers, used by Alembic.
revision: str = 'ae7bad71e1df'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create the resumes table."""
    op.create_table(
        'resumes',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('user_id', sa.String(), nullable=True),
        sa.Column('filename', sa.String(), nullable=False),
        sa.Column('file_type', sa.String(), nullable=False),
        sa.Column('storage_path', sa.String(), nullable=True),
        sa.Column('status', sa.String(), nullable=False, server_default='pending'),
        sa.Column('extracted_text', sa.Text(), nullable=True),
        sa.Column('parsed_profile', JSONB(), nullable=True),
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text('now()'),
        ),
        sa.Column(
            'updated_at',
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text('now()'),
        ),
    )
    # Index on user_id for fast per-user lookups
    op.create_index('ix_resumes_id', 'resumes', ['id'])
    op.create_index('ix_resumes_user_id', 'resumes', ['user_id'])


def downgrade() -> None:
    """Drop the resumes table."""
    op.drop_index('ix_resumes_user_id', table_name='resumes')
    op.drop_index('ix_resumes_id', table_name='resumes')
    op.drop_table('resumes')
