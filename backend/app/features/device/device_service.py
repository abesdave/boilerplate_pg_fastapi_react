import logging
from typing import List

from fastapi import HTTPException, status

from app.models import Device, User

from app.features.device import device_repository

from app.core.utilities import encode_jwt


async def get_devices() -> List[Device]:
    try:
        return await device_repository.get_devices()
    except Exception as e:
        logging.error(repr(e))
        raise e
