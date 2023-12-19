"""Test user router"""
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from okta_jwt.jwt import validate_token

from .router import router

app = FastAPI()
app.include_router(router)


@pytest.fixture
def mock_okta(mocker):
    """mock okta"""
    mock = Mock(spec=validate_token)
    mocker.patch("validate_token", return_value=mock)
    return mock


client = TestClient(app)

res = {"id": "id", "fullname": "fullname", "email": "mail@a.b"}


def test_me():
    """test"""
    response = client.get("/me")
    assert response.json() == res
    assert response.status_code == 200
