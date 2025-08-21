import sys
import json
sys.path.insert(0, '../src')
from src.data_fetching import data_collector


def get_most_rated(all_movies, amount_of_movies): 
  all_movies_copy = all_movies
  max_vote_count = max(movie["vote_count"] for movie in all_movies)
  top_list = []

  while len(top_list) < amount_of_movies:
    max_vote_indices = [i for i, val in enumerate(all_movies_copy) if val["vote_count"] == max_vote_count]
    if len(max_vote_indices) > 0:
      new_list = (all_movies_copy[i] for i in max_vote_indices)
      top_list.append(*new_list)
    max_vote_count = max_vote_count - 1

  return list(top_list)


with open('data/movies.json') as f:
    d = json.load(f)

most_rated = get_most_rated(d, 100)

data_collector.save_data(most_rated, "most_rated")
