"""'coins'

Revision ID: 2a8adb47a810
Revises: e021f325be3d
Create Date: 2020-05-18 11:50:01.843747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a8adb47a810'
down_revision = 'e021f325be3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('land_coin', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'land_coin')
    # ### end Alembic commands ###