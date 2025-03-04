import pytest
from fastapi import status


@pytest.mark.anyio
async def test_post_link(get_client):
    response = await get_client.post(
        url="/urls", json={"long_url": "www.example.com/start-service"}
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.anyio
async def test_get_redirect_link(get_client, create_link_for_tests):
    short_url = create_link_for_tests.json()["short_url"]
    response = await get_client.get(url=f"/urls/{short_url}")
    assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT
    assert response.headers["Location"] == "http://127.0.0.1:8000/docs"
