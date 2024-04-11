import os

from sqlalchemy import create_engine


class Database:
    db_url = (
        f"postgresql://{os.environ.get('POSTGRES_USER')}"
        f":{os.environ.get('POSTGRES_PASSWORD')}@{os.environ.get('POSTGRES_HOST')}"
        f":{os.environ.get('POSTGRES_PORT')}/{os.environ.get('POSTGRES_DB')}"
    )
    print("Creating connection to database.")
    engine = create_engine(db_url, echo=True)


database = Database()
