import os

from sqlmodel import SQLModel, Session

from sqlalchemy.ext.asyncio import create_async_engine

# TODO(David): Refactor into settings class
db_user = os.getenv("POSTGRES_USER", "postgres")
db_user_password = os.getenv("POSTGRES_PASSWORD", "postgres")
db_name = os.getenv("POSTGRES_DB", "app")
db_port = os.getenv("POSTGRES_PORT", "5432")
db_host = os.getenv("POSTGRES_HOST", "database")
url = f"postgresql+asyncpg://{db_user}:{db_user_password}@{db_host}:{db_port}/{db_name}"
db_engine = create_async_engine(url, echo=True)


# async def init():
#     async with db_engine.begin() as db_conn:
#         # await conn.run_sync(SQLModel.metadata.drop_all)
#         await db_conn.run_sync(SQLModel.metadata.create_all)


# def get_session():
#     with Session(db_engine) as session:
#         yield session
