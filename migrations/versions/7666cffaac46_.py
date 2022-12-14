"""empty message

Revision ID: 7666cffaac46
Revises: 7fa0653a465a
Create Date: 2022-12-06 11:31:49.922762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7666cffaac46'
down_revision = '7fa0653a465a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('changebio', sa.String(length=140), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('changebio')

    # ### end Alembic commands ###
