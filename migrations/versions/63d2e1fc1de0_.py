"""empty message

Revision ID: 63d2e1fc1de0
Revises: aea1dda7cc96
Create Date: 2023-10-14 03:58:56.518215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63d2e1fc1de0'
down_revision = 'aea1dda7cc96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    # ### end Alembic commands ###
