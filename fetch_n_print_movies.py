import json
import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # This is to load your API keys from .env

TMDB_TRENDING_PATH = 'trending/all/day'
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
#print(json_data)

# Convert json_data to a formatted pretty
# json string that is easy for humans to read.
# Mouse over function to get definition of indent and sort_keys
pretty_json_data = json.dumps(json_data, indent=4, sort_keys=True)
#print(pretty_json_data)

daily_trending = json_data
# Add Parsing Code Here

#movies = [item for item in daily_trending['results'] if item['media_type'] == 'movie']
media = []

for item in daily_trending['results']:
    if item['media_type'] == 'movie':
        new = {'title': item['title'], 'popularity': item['popularity'], 'vote_count': item['vote_count']}
        media.append(new)
    else:
        new = {'title': item['name'], 'popularity': item['popularity'], 'vote_count': item['vote_count']}
        media.append(new)

for item in media:
    print(f"Title/Name: {item['title']:<50}Popularity: {item['popularity']:<30}Vote Count: {item['vote_count']:.1f}")

        

        