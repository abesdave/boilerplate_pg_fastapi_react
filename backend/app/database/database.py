import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

db_url = (
    f"postgresql+psycopg2://{os.environ.get('DB_USER')}"
    f":{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}"
    f":{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"
)

engine = create_async_engine(db_url)

AsyncSessionLocal = async_sessionmaker(
    autoflush=False, autocommit=False, bind=engine, expire_on_commit=False
)


async def get_db_session():
    return AsyncSessionLocal()
