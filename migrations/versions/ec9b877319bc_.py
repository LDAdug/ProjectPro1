"""empty message

Revision ID: ec9b877319bc
Revises: 4f3471ad6eef
Create Date: 2022-12-04 16:49:31.323159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec9b877319bc'
down_revision = '4f3471ad6eef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=True),
    sa.Column('name', sa.String(length=15), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_post_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_post_timestamp'))

    op.drop_table('post')
    op.drop_table('followers')
    op.drop_table('user')
    # ### end Alembic commands ###
