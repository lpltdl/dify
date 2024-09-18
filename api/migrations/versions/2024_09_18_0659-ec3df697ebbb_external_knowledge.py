"""external_knowledge

Revision ID: ec3df697ebbb
Revises: 675b5321501b
Create Date: 2024-09-18 06:59:54.048478

"""
from alembic import op
import models as models
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ec3df697ebbb'
down_revision = '675b5321501b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('external_api_templates',
    sa.Column('id', models.types.StringUUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('tenant_id', models.types.StringUUID(), nullable=False),
    sa.Column('settings', sa.Text(), nullable=True),
    sa.Column('created_by', models.types.StringUUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('updated_by', models.types.StringUUID(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.PrimaryKeyConstraint('id', name='external_api_template_pkey')
    )
    with op.batch_alter_table('external_api_templates', schema=None) as batch_op:
        batch_op.create_index('external_api_templates_name_idx', ['name'], unique=False)
        batch_op.create_index('external_api_templates_tenant_idx', ['tenant_id'], unique=False)

    op.create_table('external_knowledge_bindings',
    sa.Column('id', models.types.StringUUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('tenant_id', models.types.StringUUID(), nullable=False),
    sa.Column('external_api_template_id', models.types.StringUUID(), nullable=False),
    sa.Column('dataset_id', models.types.StringUUID(), nullable=False),
    sa.Column('external_knowledge_id', sa.Text(), nullable=False),
    sa.Column('created_by', models.types.StringUUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('updated_by', models.types.StringUUID(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.PrimaryKeyConstraint('id', name='external_knowledge_bindings_pkey')
    )
    with op.batch_alter_table('external_knowledge_bindings', schema=None) as batch_op:
        batch_op.create_index('external_knowledge_bindings_dataset_idx', ['dataset_id'], unique=False)
        batch_op.create_index('external_knowledge_bindings_external_api_template_idx', ['external_api_template_id'], unique=False)
        batch_op.create_index('external_knowledge_bindings_external_knowledge_idx', ['external_knowledge_id'], unique=False)
        batch_op.create_index('external_knowledge_bindings_tenant_idx', ['tenant_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table('external_knowledge_bindings', schema=None) as batch_op:
        batch_op.drop_index('external_knowledge_bindings_tenant_idx')
        batch_op.drop_index('external_knowledge_bindings_external_knowledge_idx')
        batch_op.drop_index('external_knowledge_bindings_external_api_template_idx')
        batch_op.drop_index('external_knowledge_bindings_dataset_idx')

    op.drop_table('external_knowledge_bindings')
    with op.batch_alter_table('external_api_templates', schema=None) as batch_op:
        batch_op.drop_index('external_api_templates_tenant_idx')
        batch_op.drop_index('external_api_templates_name_idx')

    op.drop_table('external_api_templates')
    # ### end Alembic commands ###
