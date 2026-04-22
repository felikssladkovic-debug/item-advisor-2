import pytest


pytestmark = pytest.mark.anyio


async def test_admin_users_endpoint_as_manager(client):
    await client.post(
        "/api/v1/auth/login",
        json={"email": "manager@example.com", "password": "manager123"},
    )

    response = await client.get("/api/v1/admin/users")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]) == 2
    assert {user["role"] for user in body["data"]} == {"manager", "user"}


async def test_admin_users_endpoint_as_non_manager_forbidden(client):
    await client.post(
        "/api/v1/auth/login",
        json={"email": "user@example.com", "password": "user123"},
    )

    response = await client.get("/api/v1/admin/users")

    assert response.status_code == 403
