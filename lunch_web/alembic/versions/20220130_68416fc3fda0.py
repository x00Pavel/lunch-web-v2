"""update relationships

Revision ID: 68416fc3fda0
Revises: 3cdd22231811
Create Date: 2022-01-30 20:39:46.098944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68416fc3fda0'
down_revision = '3cdd22231811'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_dishes_menu_id_menus', 'dishes', type_='foreignkey')
    op.create_foreign_key(op.f('fk_dishes_menu_id_menus'), 'dishes', 'menus', ['menu_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_dishes_menu_id_menus'), 'dishes', type_='foreignkey')
    op.create_foreign_key('fk_dishes_menu_id_menus', 'dishes', 'menus', ['menu_id'], ['id'])
    # ### end Alembic commands ###
