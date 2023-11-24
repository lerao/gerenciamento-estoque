"""Inicialização

Revision ID: 308a976e95d1
Revises: 4bc3a1c15309
Create Date: 2023-11-16 21:57:42.422992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '308a976e95d1'
down_revision = '4bc3a1c15309'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('produtos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=True),
    sa.Column('qtd', sa.Integer(), nullable=True),
    sa.Column('tipo', sa.String(length=15), nullable=True),
    sa.Column('preco', sa.Float(), nullable=True),
    sa.Column('descricao', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produtos')
    # ### end Alembic commands ###
