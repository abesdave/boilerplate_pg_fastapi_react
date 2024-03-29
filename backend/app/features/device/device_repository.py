from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.orm import selectinload

from app.core.database import db_engine
from app.models import Device


async def get_devices() -> List[Device]:
    async with AsyncSession(db_engine) as session:
        query = select(Device).options(selectinload(Device.device_data))
        result = await session.exec(query)
        devices = result.all()
        return devices
