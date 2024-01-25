"""comment

Revision ID: 7f76b6438ca4
Revises: c9dc56b687ec
Create Date: 2024-01-25 15:11:03.913096

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f76b6438ca4'
down_revision: Union[str, None] = 'c9dc56b687ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
