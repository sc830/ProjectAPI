import json
import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # This is to load your API keys from .env

TMDB_TRENDING_PATH = 'trending/all/day'
TMDB_ACTOR_PATH = 'trending/person/day'
TMDB_TRENDING_API_REQUEST = f'https://api.themoviedb.org/3/{TMDB_TRENDING_PATH}?'
TMDB_ACTOR_API_REQUEST = f'https://api.themoviedb.org/3/{TMDB_ACTOR_PATH}?'


response = requests.get(
    TMDB_TRENDING_API_REQUEST,
    params={
        'api_key': os.getenv('TMDB_API_KEY')
    }
)
# Encodes response into a python json dictionary.
trending_json_data = response.json()


response = requests.get(
    TMDB_ACTOR_API_REQUEST,
    params={
        'api_key': os.getenv('TMDB_API_KEY')
    }
)
# Encodes response into a python json dictionary.
actor_json_data = response.json()

daily_trending = trending_json_data
actors = actor_json_data
# Add Parsing Code Here

#movies = [item for item in daily_trending['results'] if item['all_results_type'] == 'movie']
all_results = []

for item in daily_trending['results']:
    if item['media_type'] == 'movie':
        new = {'name': item['title'], 'popularity': item['popularity'], 'vote_count': item['vote_count']}
        all_results.append(new)
    else:
        new = {'name': item['name'], 'popularity': item['popularity'], 'vote_count': item['vote_count']}
        all_results.append(new)

for actor in actors['results']:
    if actor['known_for'][0]['media_type'] == 'movie':
        new = {'name': actor['known_for'][0]['title'], 'popularity': actor['known_for'][0]['popularity'], 'vote_count': actor['known_for'][0]['vote_count']}
    else:
        new = {'name': actor['known_for'][0]['name'], 'popularity': actor['known_for'][0]['popularity'], 'vote_count': actor['known_for'][0]['vote_count']}

for item in all_results:
    print(f"Title/Name: {item['name']:<50}Popularity: {item['popularity']:<30}Vote Count: {item['vote_count']:.1f}")

        

        