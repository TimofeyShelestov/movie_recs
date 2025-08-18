import os
from dotenv import load_dotenv

load_dotenv()

# API
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
TMDB_BASE_URL = "https://api.themoviedb.org/3"
