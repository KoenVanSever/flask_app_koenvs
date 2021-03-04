"""initial

Revision ID: 4c4bc63f3b65
Revises: 
Create Date: 2021-03-03 21:53:53.825624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c4bc63f3b65'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=512), nullable=False),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('dimming_curves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('color_type', sa.String(length=128), nullable=False),
    sa.Column('filename', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('filename'),
    sa.UniqueConstraint('name')
    )
    op.create_table('parameters_files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('csv_name', sa.String(length=128), nullable=False),
    sa.Column('short_name', sa.String(length=64), nullable=False),
    sa.Column('light_family', sa.String(length=32), nullable=True),
    sa.Column('byte_128', sa.SmallInteger(), nullable=False),
    sa.Column('byte_129', sa.SmallInteger(), nullable=False),
    sa.Column('byte_130', sa.SmallInteger(), nullable=False),
    sa.Column('byte_131', sa.SmallInteger(), nullable=False),
    sa.Column('byte_132', sa.SmallInteger(), nullable=False),
    sa.Column('byte_133', sa.SmallInteger(), nullable=False),
    sa.Column('byte_134', sa.SmallInteger(), nullable=False),
    sa.Column('byte_135', sa.SmallInteger(), nullable=False),
    sa.Column('byte_136', sa.SmallInteger(), nullable=False),
    sa.Column('byte_137/138', sa.SmallInteger(), nullable=False),
    sa.Column('byte_139', sa.SmallInteger(), nullable=False),
    sa.Column('byte_140', sa.SmallInteger(), nullable=False),
    sa.Column('byte_141', sa.SmallInteger(), nullable=False),
    sa.Column('byte_142', sa.SmallInteger(), nullable=False),
    sa.Column('byte_143', sa.SmallInteger(), nullable=False),
    sa.Column('byte_144', sa.SmallInteger(), nullable=False),
    sa.Column('byte_145', sa.SmallInteger(), nullable=False),
    sa.Column('byte_146', sa.SmallInteger(), nullable=False),
    sa.Column('byte_147/148', sa.SmallInteger(), nullable=False),
    sa.Column('byte_149/150', sa.SmallInteger(), nullable=False),
    sa.Column('byte_151/152', sa.SmallInteger(), nullable=False),
    sa.Column('byte_153/154', sa.SmallInteger(), nullable=False),
    sa.Column('byte_155/156', sa.SmallInteger(), nullable=False),
    sa.Column('byte_157/158', sa.SmallInteger(), nullable=False),
    sa.Column('byte_159/160', sa.SmallInteger(), nullable=False),
    sa.Column('byte_161/162', sa.SmallInteger(), nullable=False),
    sa.Column('byte_163', sa.SmallInteger(), nullable=False),
    sa.Column('byte_164', sa.SmallInteger(), nullable=False),
    sa.Column('byte_165', sa.SmallInteger(), nullable=False),
    sa.Column('byte_166', sa.SmallInteger(), nullable=False),
    sa.Column('byte_167', sa.SmallInteger(), nullable=False),
    sa.Column('byte_168', sa.SmallInteger(), nullable=False),
    sa.Column('byte_169/170', sa.SmallInteger(), nullable=False),
    sa.Column('byte_171', sa.SmallInteger(), nullable=False),
    sa.Column('byte_172', sa.SmallInteger(), nullable=False),
    sa.Column('byte_173', sa.SmallInteger(), nullable=False),
    sa.Column('byte_174', sa.SmallInteger(), nullable=False),
    sa.Column('byte_175/176', sa.SmallInteger(), nullable=False),
    sa.Column('byte_177/178', sa.SmallInteger(), nullable=False),
    sa.Column('byte_179/180', sa.SmallInteger(), nullable=False),
    sa.Column('byte_181/182', sa.SmallInteger(), nullable=False),
    sa.Column('byte_183/184', sa.SmallInteger(), nullable=False),
    sa.Column('byte_185/186', sa.SmallInteger(), nullable=False),
    sa.Column('byte_187/188', sa.SmallInteger(), nullable=False),
    sa.Column('byte_189/190', sa.SmallInteger(), nullable=False),
    sa.Column('byte_191/192', sa.SmallInteger(), nullable=False),
    sa.Column('byte_193/194', sa.SmallInteger(), nullable=False),
    sa.Column('byte_195/196', sa.SmallInteger(), nullable=False),
    sa.Column('byte_197/198', sa.SmallInteger(), nullable=False),
    sa.Column('byte_199/200', sa.SmallInteger(), nullable=False),
    sa.Column('byte_201', sa.SmallInteger(), nullable=False),
    sa.Column('byte_202/203', sa.SmallInteger(), nullable=False),
    sa.Column('byte_204/205', sa.SmallInteger(), nullable=False),
    sa.Column('byte_206', sa.SmallInteger(), nullable=False),
    sa.Column('byte_207', sa.SmallInteger(), nullable=False),
    sa.Column('byte_208/209', sa.SmallInteger(), nullable=False),
    sa.Column('byte_210/211', sa.SmallInteger(), nullable=False),
    sa.Column('byte_212', sa.SmallInteger(), nullable=False),
    sa.Column('byte_213', sa.SmallInteger(), nullable=False),
    sa.Column('byte_214', sa.SmallInteger(), nullable=False),
    sa.Column('byte_215', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('csv_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parameters_files')
    op.drop_table('dimming_curves')
    op.drop_table('auth_user')
    # ### end Alembic commands ###