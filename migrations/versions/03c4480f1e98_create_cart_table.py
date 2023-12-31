"""create cart table

Revision ID: 03c4480f1e98
Revises: 
Create Date: 2023-12-21 11:27:29.520644

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '03c4480f1e98'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=50), nullable=True),
    sa.Column('contents', sqlite.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_cart_public_id'), ['public_id'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_cart_public_id'))

    op.drop_table('cart')
    # ### end Alembic commands ###
