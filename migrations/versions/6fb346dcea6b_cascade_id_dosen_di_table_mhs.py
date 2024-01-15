"""cascade id dosen di table mhs

Revision ID: 6fb346dcea6b
Revises: 43243eb56f99
Create Date: 2024-01-15 11:15:32.687147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fb346dcea6b'
down_revision = '43243eb56f99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint('mahasiswa_ibfk_1', type_='foreignkey')
        batch_op.drop_constraint('mahasiswa_ibfk_2', type_='foreignkey')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_dua'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_satu'], ['id'], onupdate='CASCADE', ondelete='SET NULL')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('mahasiswa_ibfk_2', 'dosen', ['dosen_dua'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
        batch_op.create_foreign_key('mahasiswa_ibfk_1', 'dosen', ['dosen_satu'], ['id'], onupdate='CASCADE', ondelete='CASCADE')

    # ### end Alembic commands ###