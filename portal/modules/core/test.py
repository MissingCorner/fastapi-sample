"""Test config router"""
from fastapi import FastAPI
from fastapi.testclient import TestClient

from .config import Settings, configs
from .router import router

app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_read_info():
    """test"""
    res = {"oktaDomain": "domain", "oktaClientId": "client-id"}

    def configs_override():
        """override"""
        print("HERE")
        return Settings(
            OKTA_CLIENT_ID=res["oktaClientId"], OKTA_DOMAIN=res["oktaDomain"]
        )

    app.dependency_overrides[configs] = configs_override

    response = client.get("/_info")
    assert response.status_code == 200
    assert response.json() == res


def test_root():
    """test"""
    response = client.get("/")
    assert response.json() == {"Hello": "World"}
    assert response.status_code == 200
