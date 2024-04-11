import os
from sqlalchemy import create_engine

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
db_url = (
    f"postgresql+psycopg2://{os.environ.get('DB_USER')}"
    f":{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}"
    f":{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"
)

engine = create_engine(db_url)
