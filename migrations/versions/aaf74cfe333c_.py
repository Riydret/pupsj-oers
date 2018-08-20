"""empty message

Revision ID: aaf74cfe333c
Revises: 65b2ae5ffa2c
Create Date: 2018-07-11 15:39:21.759444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aaf74cfe333c'
down_revision = '65b2ae5ffa2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservation', sa.Column('res_status', sa.String(length=15), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservation', 'res_status')
    # ### end Alembic commands ###