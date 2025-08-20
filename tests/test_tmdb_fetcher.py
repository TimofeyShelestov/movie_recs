import pytest
from aioresponses import aioresponses
import aiohttp
from config import settings
from src.data_fetching import tmdb_fetcher

SUCCESS_STATUS = 200
BAD_STATUS = 500

class TestSiglePageFetch(): 

  @pytest.mark.asyncio
  async def test_successful_response(self):
    headers = {
        "Content-Type": "application/json"
    }
    json_data = {
        "page": 1,
        "results": [
            {"id": 123, "title": "Test Movie", "vote_average": 8.5},
            {"id": 456, "title": "Another Movie", "vote_average": 7.2}
        ],
        "total_pages": 500,
        "total_results": 10000
    }
    session = aiohttp.ClientSession()

    with aioresponses() as mocked:
        mocked.get(f'{settings.TMDB_BASE_URL}/movie/popular?page=1&language=en-US', status=200, payload=json_data, headers=headers)

        res = await tmdb_fetcher.fetch_single_page(session, 1)

        await session.close()

        mocked.assert_called_once()
        assert res is not None
        assert res["page"] == 1
        assert len(res["results"]) == 2
        assert res["results"][0]["title"] == "Test Movie"


  # @pytest.mark.asyncio
  # async def test_error_code_res(self, monkeypatch):
  #   mock_session = AsyncMock()
  #   mock_response = AsyncMock()
  #   mock_response.status = BAD_STATUS

  #   mock_session.get.return_value = AsyncMock()
  #   mock_session.get.return_value.__aenter__.return_value = mock_response
  #   mock_session.get.return_value.__aexit__.return_value = None

  #   monkeypatch.setattr('src.data_fetching.tmdb_fetcher.aiohttp.ClientSession', lambda : mock_session)

  #   result = await tmdb_fetcher.fetch_single_page(mock_session, 1)

  #   assert result is None

  #   mock_session.get.assert_called_once()
  #   call_args = mock_session.get.call_args
  #   assert "Authorization" in call_args[1]["headers"]

