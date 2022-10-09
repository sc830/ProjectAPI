import json
import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # This is to load your API keys from .env

TMDB_TRENDING_PATH = 'trending/movie/week'
TMDB_SEARCH_API_REQUEST = f'https://api.themoviedb.org/3/{TMDB_TRENDING_PATH}?'

#def get_top_10_weekly_trending_movies():
response = requests.get(
    TMDB_SEARCH_API_REQUEST,
    params={
        'api_key': os.getenv('TMDB_API_KEY')
    }
)
# Encodes response into a python json dictionary.
json_data = response.json()
print(json_data)

# Convert json_data to a formatted pretty
# json string that is easy for humans to read.
# Mouse over function to get definition of indent and sort_keys
pretty_json_data = json.dumps(json_data, indent=4, sort_keys=True)
print(pretty_json_data)

weekly_trending_movie_object = json_data
# Add Parsing Code Here