import asyncio
from src.data_fetching import tmdb_fetcher

asyncio.run(tmdb_fetcher.fetch_pages_async(1))