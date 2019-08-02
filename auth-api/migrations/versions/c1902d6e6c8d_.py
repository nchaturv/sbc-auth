"""empty message

Revision ID: c1902d6e6c8d
Revises: 0f934590ef1d
Create Date: 2019-07-29 16:11:00.223851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1902d6e6c8d'
down_revision = '0f934590ef1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entity', sa.Column('contact1_id', sa.Integer(), nullable=True))
    op.add_column('entity', sa.Column('contact2_id', sa.Integer(), nullable=True))
    op.drop_constraint('entity_contact2_fkey', 'entity', type_='foreignkey')
    op.drop_constraint('entity_contact1_fkey', 'entity', type_='foreignkey')
    op.create_foreign_key(None, 'entity', 'contact', ['contact1_id'], ['id'])
    op.create_foreign_key(None, 'entity', 'contact', ['contact2_id'], ['id'])
    op.drop_column('entity', 'contact2')
    op.drop_column('entity', 'contact1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entity', sa.Column('contact1', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('entity', sa.Column('contact2', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'entity', type_='foreignkey')
    op.drop_constraint(None, 'entity', type_='foreignkey')
    op.create_foreign_key('entity_contact1_fkey', 'entity', 'contact', ['contact1'], ['id'])
    op.create_foreign_key('entity_contact2_fkey', 'entity', 'contact', ['contact2'], ['id'])
    op.drop_column('entity', 'contact2_id')
    op.drop_column('entity', 'contact1_id')
    # ### end Alembic commands ###
