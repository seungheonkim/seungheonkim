"""empty message

Revision ID: 194fb8c9a982
Revises: 
Create Date: 2022-02-22 00:46:31.386138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '194fb8c9a982'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('pwd', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer')
    # ### end Alembic commands ###
