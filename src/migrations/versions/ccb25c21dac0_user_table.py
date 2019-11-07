"""user table

Revision ID: ccb25c21dac0
Revises: 1fc058233de8
Create Date: 2019-07-31 12:03:04.075782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccb25c21dac0'
down_revision = '1fc058233de8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dataset', sa.Column('version', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dataset', 'version')
    # ### end Alembic commands ###
