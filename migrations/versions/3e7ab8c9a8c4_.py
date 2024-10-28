"""empty message

Revision ID: 3e7ab8c9a8c4
Revises: 3a334fd26a54
Create Date: 2024-10-24 13:12:37.290494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e7ab8c9a8c4'
down_revision = '3a334fd26a54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_name', sa.String(length=100), nullable=False),
    sa.Column('originality', sa.Integer(), nullable=False),
    sa.Column('gameplay', sa.Integer(), nullable=False),
    sa.Column('story', sa.Integer(), nullable=False),
    sa.Column('bugs', sa.Integer(), nullable=False),
    sa.Column('graphics', sa.Integer(), nullable=False),
    sa.Column('sound', sa.Integer(), nullable=False),
    sa.Column('music', sa.Integer(), nullable=False),
    sa.Column('design', sa.Integer(), nullable=False),
    sa.Column('atmosphere', sa.Integer(), nullable=False),
    sa.Column('general_impression', sa.Integer(), nullable=False),
    sa.Column('total_score', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('game_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rating')
    # ### end Alembic commands ###
