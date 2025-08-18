import json
from .tmdb_fetcher import fetch_pages_async

async def collect_movies(pages):
  res = await fetch_pages_async(pages) 
  raw_data = []

  for page in res:
    raw_data.extend(page["results"])

  with open("data/raw_movies.json", "w") as f:
          json.dump(raw_data, f, indent=2)

  movies = [
    {
        "id": movie["id"],
        "title": movie["title"],
        "genre_ids": movie["genre_ids"],
        "vote_average": movie["vote_average"],
        "vote_count": movie["vote_count"]
    }
    for movie in raw_data
  ]

  with open("data/movies.json", "w") as f:
          json.dump(movies, f, indent=2)