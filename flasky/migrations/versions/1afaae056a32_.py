"""empty message

Revision ID: 1afaae056a32
Revises: 1cfe4410f69e
Create Date: 2017-01-15 01:55:56.248348

"""

# revision identifiers, used by Alembic.
revision = '1afaae056a32'
down_revision = '1cfe4410f69e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about_me', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('loctaion', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('member_since', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('name', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'name')
    op.drop_column('users', 'member_since')
    op.drop_column('users', 'loctaion')
    op.drop_column('users', 'last_seen')
    op.drop_column('users', 'about_me')
    ### end Alembic commands ###