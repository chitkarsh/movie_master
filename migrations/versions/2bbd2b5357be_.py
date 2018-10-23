"""empty message

Revision ID: 2bbd2b5357be
Revises: 0d0a1c9ee189
Create Date: 2018-10-21 17:23:31.801000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2bbd2b5357be'
down_revision = '0d0a1c9ee189'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('director',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('pd_alerts',
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], )
    )
    op.add_column(u'genre', sa.Column('name', sa.String(length=50), nullable=False))
    op.drop_index('genre', table_name='genre')
    op.create_unique_constraint(None, 'genre', ['name'])
    op.drop_column(u'genre', 'genre')
    op.drop_index('director', table_name='movie')
    op.drop_constraint(u'movie_ibfk_1', 'movie', type_='foreignkey')
    op.drop_column(u'movie', 'director')
    op.drop_column(u'movie', 'genre_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'movie', sa.Column('genre_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column(u'movie', sa.Column('director', mysql.VARCHAR(length=80), nullable=False))
    op.create_foreign_key(u'movie_ibfk_1', 'movie', 'genre', ['genre_id'], ['id'])
    op.create_index('director', 'movie', ['director'], unique=True)
    op.add_column(u'genre', sa.Column('genre', mysql.VARCHAR(length=50), nullable=False))
    op.drop_constraint(None, 'genre', type_='unique')
    op.create_index('genre', 'genre', ['genre'], unique=True)
    op.drop_column(u'genre', 'name')
    op.drop_table('pd_alerts')
    op.drop_table('director')
    # ### end Alembic commands ###
