"""dataset table

Revision ID: 1fc058233de8
Revises: 983e82289234
Create Date: 2019-07-30 17:32:50.707278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fc058233de8'
down_revision = '983e82289234'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dataset', sa.Column('description', sa.String(length=300), nullable=True))
    op.create_index(op.f('ix_dataset_type'), 'dataset', ['type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dataset_type'), table_name='dataset')
    op.drop_column('dataset', 'description')
    # ### end Alembic commands ###
