import logging
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from app.core.database import db_engine
from app.models import User


async def get_user(username: str) -> User:
    async with AsyncSession(db_engine) as session:
        query = select(User).where(User.username == username)
        result = await session.exec(query)
        return result.one()
