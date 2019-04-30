"""Updated usermodel

Revision ID: 24d51cb4ee14
Revises: 
Create Date: 2019-04-29 18:39:21.943951

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '24d51cb4ee14'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('content', sa.String(length=2550), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('occupation')
    op.add_column('reviews', sa.Column('article_id', sa.Integer(), nullable=True))
    op.add_column('reviews', sa.Column('review', sa.String(length=255), nullable=True))
    op.create_foreign_key(None, 'reviews', 'articles', ['article_id'], ['id'])
    op.drop_column('reviews', 'posted')
    op.drop_column('reviews', 'image_path')
    op.drop_column('reviews', 'movie_title')
    op.drop_column('reviews', 'movie_id')
    op.drop_column('reviews', 'movie_review')
    op.drop_constraint('users_occupation_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'occupation_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('occupation_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_occupation_id_fkey', 'users', 'occupation', ['occupation_id'], ['id'])
    op.add_column('reviews', sa.Column('movie_review', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('reviews', sa.Column('movie_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('reviews', sa.Column('movie_title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('reviews', sa.Column('image_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('reviews', sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'review')
    op.drop_column('reviews', 'article_id')
    op.create_table('occupation',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='occupation_pkey')
    )
    op.drop_table('articles')
    # ### end Alembic commands ###
