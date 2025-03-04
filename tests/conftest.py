import pytest
from httpx import ASGITransport, AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient

from app.main import app


@pytest.fixture(autouse=True)
async def get_db():
    app.mongodb_client = AsyncIOMotorClient("mongodb://localhost:27017/")
    app.database = app.mongodb_client["test_database"]

    yield app

    app.mongodb_client.close()


@pytest.fixture()
async def get_client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/"
    ) as client:
        yield client


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture
async def create_link_for_tests(get_client):
    response = await get_client.post(
        url="/urls", json={"long_url": "http://127.0.0.1:8000/docs"}
    )
    return response
