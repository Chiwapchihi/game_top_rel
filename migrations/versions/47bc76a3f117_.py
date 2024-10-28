"""empty message

Revision ID: 47bc76a3f117
Revises: 05fc3c280b42
Create Date: 2024-10-24 15:08:44.971417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47bc76a3f117'
down_revision = '05fc3c280b42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('personal_rating', schema=None) as batch_op:
        batch_op.drop_column('game_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('personal_rating', schema=None) as batch_op:
        batch_op.add_column(sa.Column('game_name', sa.VARCHAR(length=100), nullable=False))

    # ### end Alembic commands ###