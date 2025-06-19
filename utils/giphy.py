import requests
import json
import random
import os
from dotenv import load_dotenv

load_dotenv()
giphy_API_key= os.getenv('GIPHYAPIKEY')

def get_random_gif(prompt):
  random_number = random.randint(2,50)

  url = f'https://api.giphy.com/v1/gifs/search?q={prompt}&api_key={giphy_API_key}&limit={random_number}'

  response = requests.get(url)
  json_data = response.json()

  if not json_data:
    return 'Unauthorized call to Giphy'

  #accessing the gif list
  gif_list = json_data.get('data', [])

  if not gif_list:
    return 'No GIFs found or Unauthorized call to Giphy.'

  # grab a single random  gif list
  random_gif_data = random.choice(gif_list)
  gif_url = random_gif_data.get('images', {}).get('original',{}).get('url')

  if gif_url:
    return gif_url
  else:
      return