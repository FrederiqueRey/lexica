import pytest
from unittest.mock import AsyncMock, patch
from httpx import AsyncClient, ASGITransport
from api.app import app

FAKE_WORD = {
    "id": "507f1f77bcf86cd799439011",
    "d": "<b>πατήρ</b>, father",
    "m": ["πατήρ"],
    "g": ["patr"],
    "l": ["pater"],
    "sort_key": 42,
}

FAKE_NEIGHBORS = {
    "before": [
        {"id": "507f1f77bcf86cd799439010", "m": ["πατέω"], "g": ["pateo"], "l": ["pateo"], "d": "", "sort_key": 41},
    ],
    "after": [
        {"id": "507f1f77bcf86cd799439012", "m": ["πάτημα"], "g": ["patema"], "l": ["patema"], "d": "", "sort_key": 43},
    ],
}


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


@pytest.mark.anyio
async def test_search_returns_results():
    with patch("api.routes.find_word", new=AsyncMock(return_value=[FAKE_WORD])):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.get("/word/mgl/pater")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["l"] == ["pater"]


@pytest.mark.anyio
async def test_search_returns_empty_list():
    with patch("api.routes.find_word", new=AsyncMock(return_value=[])):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.get("/word/mgl/zzzzz")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.anyio
async def test_get_word_by_id():
    with patch("api.routes.retrieve_word", new=AsyncMock(return_value=FAKE_WORD)):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.get(f"/word/{FAKE_WORD['id']}")
    assert response.status_code == 200
    assert response.json()["m"] == ["πατήρ"]


@pytest.mark.anyio
async def test_get_word_by_id_not_found():
    with patch("api.routes.retrieve_word", new=AsyncMock(return_value=None)):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.get("/word/507f1f77bcf86cd799439099")
    assert response.status_code == 404


@pytest.mark.anyio
async def test_get_neighbors():
    with patch("api.routes.retrieve_word", new=AsyncMock(return_value=FAKE_WORD)), \
         patch("api.routes.get_neighbors", new=AsyncMock(return_value=FAKE_NEIGHBORS)):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.get(f"/word/{FAKE_WORD['id']}/neighbors")
    assert response.status_code == 200
    data = response.json()
    assert "before" in data
    assert "after" in data
    assert len(data["before"]) == 1
    assert len(data["after"]) == 1


@pytest.mark.anyio
async def test_get_neighbors_word_not_found():
    with patch("api.routes.retrieve_word", new=AsyncMock(return_value=None)):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.get("/word/507f1f77bcf86cd799439099/neighbors")
    assert response.status_code == 404
