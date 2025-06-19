import discord
import json
import requests

## get all equipments
retrieve_all_equipment_url = 'https://www.exercisedb.dev/api/v1/equipments'
## get all muscles
retrieve_all_muscles_url = 'https://www.exercisedb.dev/api/v1/muscles'

def _get_all_options(url):
  results_data = []

  try:
    response = requests.get(url)
    response.raise_for_status()

    json_data = response.json()

    if not json_data.get('success', False):
      # print("API call returned success: false or unexpected structure")
      return results_data

    equipment_list_of_dicts = json_data.get('data', [])

    if not isinstance(equipment_list_of_dicts, list):
      # print('API data fields is not a list as expected')
      return results_data

    for item_dict in equipment_list_of_dicts:
      if isinstance(item_dict, dict) and 'name' in item_dict:
        results_data.append(item_dict['name'])

    # print(f"DEBUG(get_all_equipment_options): Final results_data (list of names): {results_data}")
  except requests.exceptions.RequestException as e:
    print(f'Error fetching data from API: {e}')
  except json.JSONDecodeError as e:
    print(f"ERROR(get_all_equipment_options): Failed to decode JSON from API response: {e}")
  except Exception as e:
    # Catch any other unexpected errors
    print(f"ERROR(get_all_equipment_options): An unexpected error occurred: {e}")

  return results_data

async def _get_userinput_return_workout_options(message):
  equipment_list = _get_all_options(retrieve_all_equipment_url)
  eq_options = " :white_small_square: ".join(equipment_list)

  muscles_list = _get_all_options(retrieve_all_muscles_url)
  musc_options = " :black_small_square: ".join(muscles_list)

  await message.channel.send("## Want to customize a workout routine? \n Here are some **equipment** options to start out with!")
  await message.channel.send(f'-# {eq_options}')
  await message.channel.send('And here are the **muscle** options to start with!')
  await message.channel.send(f'-# {musc_options}')