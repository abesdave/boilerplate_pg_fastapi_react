import logging

from typing import Annotated

from fastapi import APIRouter, Depends

from fastapi.security import OAuth2PasswordRequestForm

from app.models import Token

from app.features.login import login_service

router = APIRouter()


@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    try:
        username = form_data.username
        password = form_data.password
        authentication_token = await login_service.login(username, password)
        return authentication_token
    except Exception as e:
        logging.error(repr(e))
        raise e
