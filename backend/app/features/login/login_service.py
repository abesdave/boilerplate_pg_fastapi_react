import logging

from fastapi import HTTPException, status

from app.models import User

from app.features.login import login_repository

from app.core.utilities import encode_jwt


async def login(username: str, password: str) -> User:
    try:
        user = await login_repository.get_user(username)

        if not user:
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR, "Authentication Error"
            )

        auth_token = await encode_jwt(user)
        return auth_token
    except Exception as e:
        logging.error(repr(e))
        raise e
