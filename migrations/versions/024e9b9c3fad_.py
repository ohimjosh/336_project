"""empty message

Revision ID: 024e9b9c3fad
Revises: 9ad508d1556f
Create Date: 2021-12-15 18:34:17.479120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '024e9b9c3fad'
down_revision = '9ad508d1556f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.drop_column('popularity')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.add_column(sa.Column('popularity', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###