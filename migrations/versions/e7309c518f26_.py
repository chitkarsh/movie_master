"""empty message

Revision ID: e7309c518f26
Revises: 9c95c37967ff
Create Date: 2018-10-21 17:26:53.214000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7309c518f26'
down_revision = '9c95c37967ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('director_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'movie', 'director', ['director_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'movie', type_='foreignkey')
    op.drop_column('movie', 'director_id')
    # ### end Alembic commands ###
