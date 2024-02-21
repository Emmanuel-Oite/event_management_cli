import os
import sys

# Add the project root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Change the import to an absolute import
from app.models import Base
from alembic import context
from sqlalchemy import engine_from_config, pool

# If the URL is specified in the environment variable, use it; otherwise, use the one from alembic.ini
sqlalchemy_url = context.get_x_argument(as_dictionary=True).get('sqlalchemy_url', context.config.get_main_option("sqlalchemy.url"))

# Configure the SQLAlchemy engine using the URL
engine = engine_from_config(
    {"sqlalchemy.url": sqlalchemy_url},
    prefix="sqlalchemy.",
    poolclass=pool.NullPool
)

# Exclude tables with 'alembic_' prefix from the migration process
def include_object(object, name, type_, reflected, compare_to):
    return not name.startswith("alembic_")

# Pass the engine, target metadata, and custom include_object function to the context
context.configure(
    connection=engine.connect(),
    target_metadata=Base.metadata,
    include_schemas=True,
    include_object=include_object
)
