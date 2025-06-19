import discord
import random
import csv

default_playlist_file = 'playlist.csv'

def __get_random_vid(file_path):
  try:
    with open(file_path, 'r') as file:
      lines = file.readlines()
      if not lines:
        return None
      return random.choice(lines).strip()
  except Exception as e:
    print(f'An error occured: {e}')
    return None

async def command_play(message):
  await message.channel.send(__get_random_vid(default_playlist_file))