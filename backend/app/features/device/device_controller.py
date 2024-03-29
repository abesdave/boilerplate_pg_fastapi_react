import logging

from typing import Annotated, Any, List

from fastapi import APIRouter, Depends

from fastapi.security import OAuth2PasswordRequestForm

from app.models import Device, Token

from app.features.device import device_service

router = APIRouter()


@router.get("/devices")
async def login() -> Any:
    try:
        devices = await device_service.get_devices()

        response = []

        for device in devices:
            device_response = {"device": device, "device_data": device.device_data}
            response.append(device_response)

        return response
    except Exception as e:
        logging.error(repr(e))
        raise e
