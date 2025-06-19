import discord
# import json
# import requests

def _get_exercises_URL(muscles_or_equipment, what):
  custom_url = f'https://exercisedb-api.vercel.app/api/v1/{muscles_or_equipment}/{what}/exercises'
  return custom_url

def _get_random_exercises(musc_equ, what):
  url = _get_exercises_URL(musc_equ, what)
  # response = requests.get(url)
  # json_data = json.loads(response.text)

  # print(url)
  return url