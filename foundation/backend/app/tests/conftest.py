import mongomock
import pytest
from httpx import ASGITransport, AsyncClient

from app.config import get_settings
from app.main import create_app
from app.repositories.users import UserRepository
from app.startup import initialize_data


@pytest.fixture(autouse=True)
def clear_settings_cache():
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()


@pytest.fixture
async def client():
    database = mongomock.MongoClient()["itemadvisor_test"]
    initialize_data(UserRepository(database), get_settings())
    app = create_app(test_database=database)
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as test_client:
        yield test_client
