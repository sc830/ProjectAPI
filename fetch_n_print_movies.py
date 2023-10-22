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


all_results = []
movies = []
tv = []
actor_list = []

for item in daily_trending['results']:
    if item['media_type'] == 'movie':
        new = {'name': item['title'], 'popularity': item['popularity'], 'vote_count': item['vote_count'], 'vote_avg': item['vote_average']}
        all_results.append(new)
        movies.append(new)
    else:
        new = {'name': item['name'], 'popularity': item['popularity'], 'vote_count': item['vote_count'], 'vote_avg': item['vote_average']}
        all_results.append(new)
        tv.append(new)

for actor in actors['results']:
    if actor['known_for'][0]['media_type'] == 'movie':
        new = {'name': actor['known_for'][0]['title'], 'popularity': actor['known_for'][0]['popularity'], 'vote_count': actor['known_for'][0]['vote_count']}
        all_results.append(new)
        new_actor = {'name': actor['name'], 'popularity' : actor['popularity']}
        actor_list.append(new_actor)
    else:
        new = {'name': actor['known_for'][0]['name'], 'popularity': actor['known_for'][0]['popularity'], 'vote_count': actor['known_for'][0]['vote_count']}
        all_results.append(new)
        new_actor = {'name': actor['name'], 'popularity' : actor['popularity']}
        actor_list.append(new_actor)

for item in all_results:
    print(f"Name: {item['name']:<50}Popularity: {item['popularity']:<30}Vote Count: {item['vote_count']:.1f}")

print("\nMovies sorted by vote avg:")
movies.sort(key=lambda movie: movie['vote_avg'], reverse=True)
for item in movies:
    print(f"Name: {item['name']:<50}Vote Average: {item['vote_avg']:.1f}")

print("\nTV sorted by vote avg:")
tv.sort(key=lambda item: item['vote_avg'], reverse=True)
for item in tv:
    print(f"Name: {item['name']:<50}Vote Average: {item['vote_avg']:.1f}")

print("\nActors sorted by popularity:")
actor_list.sort(key=lambda actor: actor['popularity'], reverse=True)
for item in actor_list:
    print(f"Name: {item['name']:<50}Popularity: {item['popularity']:.1f}")

        

        