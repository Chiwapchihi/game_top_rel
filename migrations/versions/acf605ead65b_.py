"""empty message

Revision ID: acf605ead65b
Revises: 3e7ab8c9a8c4
Create Date: 2024-10-24 14:16:13.888604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acf605ead65b'
down_revision = '3e7ab8c9a8c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('avg_rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_name', sa.String(length=100), nullable=False),
    sa.Column('avg_originality', sa.Integer(), nullable=False),
    sa.Column('avg_gameplay', sa.Integer(), nullable=False),
    sa.Column('avg_story', sa.Integer(), nullable=False),
    sa.Column('avg_bugs', sa.Integer(), nullable=False),
    sa.Column('avg_graphics', sa.Integer(), nullable=False),
    sa.Column('avg_sound', sa.Integer(), nullable=False),
    sa.Column('avg_music', sa.Integer(), nullable=False),
    sa.Column('avg_design', sa.Integer(), nullable=False),
    sa.Column('avg_atmosphere', sa.Integer(), nullable=False),
    sa.Column('avg_general_impression', sa.Integer(), nullable=False),
    sa.Column('avg_total_score', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('game_name')
    )
    op.drop_table('rating')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rating',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('game_name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('originality', sa.INTEGER(), nullable=False),
    sa.Column('gameplay', sa.INTEGER(), nullable=False),
    sa.Column('story', sa.INTEGER(), nullable=False),
    sa.Column('bugs', sa.INTEGER(), nullable=False),
    sa.Column('graphics', sa.INTEGER(), nullable=False),
    sa.Column('sound', sa.INTEGER(), nullable=False),
    sa.Column('music', sa.INTEGER(), nullable=False),
    sa.Column('design', sa.INTEGER(), nullable=False),
    sa.Column('atmosphere', sa.INTEGER(), nullable=False),
    sa.Column('general_impression', sa.INTEGER(), nullable=False),
    sa.Column('total_score', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('game_name')
    )
    op.drop_table('avg_rating')
    # ### end Alembic commands ###
