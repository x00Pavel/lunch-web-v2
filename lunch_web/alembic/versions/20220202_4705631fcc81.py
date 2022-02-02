"""Add day column to Dishe table

Revision ID: 4705631fcc81
Revises: 68416fc3fda0
Create Date: 2022-02-02 21:29:52.368726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4705631fcc81'
down_revision = '68416fc3fda0'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dishes', sa.Column('day', sa.Text(), nullable=False))
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dishes', 'day')
    # ### end Alembic commands ###
