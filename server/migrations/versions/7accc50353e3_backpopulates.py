"""backpopulates

Revision ID: 7accc50353e3
Revises: 268dd3e1d2b9
Create Date: 2023-11-07 13:02:51.958773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7accc50353e3'
down_revision = '268dd3e1d2b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('claims', schema=None) as batch_op:
        batch_op.add_column(sa.Column('item_id', sa.Integer(), nullable=True))
        batch_op.alter_column('comment',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
        batch_op.drop_constraint('fk_claims_item_name_items', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_claims_item_id_items'), 'items', ['item_id'], ['id'])
        batch_op.drop_column('item_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('claims', schema=None) as batch_op:
        batch_op.add_column(sa.Column('item_name', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_claims_item_id_items'), type_='foreignkey')
        batch_op.create_foreign_key('fk_claims_item_name_items', 'items', ['item_name'], ['id'])
        batch_op.alter_column('comment',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.drop_column('item_id')

    # ### end Alembic commands ###
