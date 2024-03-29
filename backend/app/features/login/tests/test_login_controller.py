from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

import pytest

from app.models import Token

pytest_plugins = ("pytest_asyncio",)

from app.features.login import login_controller


@pytest.mark.asyncio
async def test_successful_login(monkeypatch):
    mock_token = Token(token="mock_token", type="Bearer")

    async def login_service_login_mock(username: str, password: str) -> Token:
        return mock_token

    monkeypatch.setattr(
        "app.features.login.login_service.login", login_service_login_mock
    )
    form_data = OAuth2PasswordRequestForm(
        username="admin@admin.com", password="p4ssw0rd"
    )

    response_token = await login_controller.login(form_data)
    assert response_token == mock_token


@pytest.mark.asyncio
async def test_un_successful_login(monkeypatch):
    async def login_service_login_mock(username: str, password: str) -> Token:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR, "Authentication Error"
        )

    monkeypatch.setattr(
        "app.features.login.login_service.login", login_service_login_mock
    )

    form_data = OAuth2PasswordRequestForm(
        username="admin@admin.com", password="p4ssw0rd"
    )

    try:
        response_token = await login_controller.login(form_data)
    except HTTPException as e:
        assert e.status_code == 500
        assert e.detail == "Authentication Error"
