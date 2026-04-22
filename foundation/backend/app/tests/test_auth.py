import pytest


pytestmark = pytest.mark.anyio


async def test_login_success(client):
    response = await client.post(
        "/api/v1/auth/login",
        json={"email": "manager@example.com", "password": "manager123"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["data"]["authenticated"] is True
    assert body["data"]["user"]["email"] == "manager@example.com"


async def test_login_failure(client):
    response = await client.post(
        "/api/v1/auth/login",
        json={"email": "manager@example.com", "password": "wrong-password"},
    )

    assert response.status_code == 401


async def test_me_authenticated(client):
    await client.post(
        "/api/v1/auth/login",
        json={"email": "manager@example.com", "password": "manager123"},
    )

    response = await client.get("/api/v1/auth/me")

    assert response.status_code == 200
    body = response.json()
    assert body["data"]["authenticated"] is True
    assert body["data"]["user"]["role"] == "manager"


async def test_me_unauthenticated(client):
    response = await client.get("/api/v1/auth/me")

    assert response.status_code == 200
    body = response.json()
    assert body["data"]["authenticated"] is False
    assert body["data"]["user"] is None
