## !eq [equipment name]
##For example, `!eq upper body ergometer`

import discord
import requests
import json

import random

from utils.workout_routine import _get_random_exercises
from commands.randExercise import __get_random_exercise_no_equipment

def __get_specialized_equipment_exercise(equipment_name_str):
  arguments_string = equipment_name_str

  # print(_get_random_exercises('equipments', arguments_string))
  url = _get_random_exercises('equipments', arguments_string)

  response = requests.get(url)
  json_data = json.loads(response.text)

  if not json_data:
    return 'Something went wrong with json request to exercisedb api'

  ##accessing the exercise list
  exercises = json_data['data']['exercises']

  results_data = []

  # Check if the list is not empty before trying to get a random index
  if exercises:
      random_index = random.randrange(len(exercises))

      random_exercise = exercises[random_index]

      name = random_exercise.get('name')
      instructions = random_exercise.get('instructions')

      results_data.append({
        'name': name,
        'instructions': instructions,
      })

      # print(results_data)
      return results_data
  else:
      return 'No exercises found'


def _clean_formatted_instructions(instructions: list[str]) -> str:
  if not instructions:
    return "No instructions available"

  cleaned_steps = []
  for step in instructions:
    if isinstance(step, str):
        if step.lower().startswith("step:") and ' ' in step:
            cleaned_steps.append(step.split(' ', 1)[1].strip())
        else:
            cleaned_steps.append(step.strip())
    else:
        print(f"WARNING: Non-string instruction step encountered: {step}")
        cleaned_steps.append(str(step).strip())
  return "\n".join([f"- {step_clean}" for step_clean in cleaned_steps]) + "\n"

def _process_raw_exercise_details(raw_exercise_dict: dict) -> dict | None:
   name = raw_exercise_dict.get('name')
   instructions = raw_exercise_dict.get('instructions')

   if not name:
      print(f'ERROR: No name found')
      return None

   instructions_text = _clean_formatted_instructions(instructions)

   return {
      'name': name.upper(),
      'value': instructions_text
   }

## EQUIPMENT
async def get_exercise_embed_field_data_with_equipment(equipment_name: str):
  random_equip_exercise_details = __get_specialized_equipment_exercise(equipment_name)
  if not random_equip_exercise_details or not isinstance(random_equip_exercise_details, list):
    return None

  return _process_raw_exercise_details(random_equip_exercise_details[0])

## NO EQUIPMENT
async def get_exercise_embed_field_data_no_equipment() -> dict | None:
  raw_exercises = __get_random_exercise_no_equipment()
  return _process_raw_exercise_details(raw_exercises[0])




async def specialized_eq_routine(message):

  ## start forming the embed text
  embed = discord.Embed(title='✧ദ്ദി( ˶^ᗜ^˶ ) Your Specialized :man_lifting_weights: Equipment :woman_lifting_weights: Routine', color=discord.Color.blue())

  # grab equipment name here
  parts = message.content.lower().split(' ', 1)
  if len(parts) < 2:
    await message.channel.send("Please provide an equipment name, e.g., `!eq upper body ergometer`")
    return
  equipment_name = parts[1].strip()



  ##exercise body - looping same steps twice
  for i in range(2):

    ## with the equipment
    eq_field_data = await get_exercise_embed_field_data_with_equipment(equipment_name)
    if eq_field_data:
      embed.add_field(name=f'{eq_field_data["name"]}', value=f'{eq_field_data["value"]}')
    else:
      embed.add_field(name=f'Equipment Exercise {i+1}:', value=f"Could not find an equipment-specific exercise for '{equipment_name}'.")

    # NO equipment
    another_no_eq_field_data = await get_exercise_embed_field_data_no_equipment()
    if another_no_eq_field_data:
      embed.add_field(name=f'{another_no_eq_field_data["name"]}', value=f'{another_no_eq_field_data["value"]}')
    else:
      embed.add_field(name=f'Equipment Exercise {i+1}:', value=f"Let's repeat that :)'.")

    ##THIRD EQUIPMENT
    sec_eq_field_data = await get_exercise_embed_field_data_with_equipment(equipment_name)
    if eq_field_data:
      embed.add_field(name=f'{sec_eq_field_data["name"]}', value=f'{sec_eq_field_data["value"]}', inline=False)
    else:
      embed.add_field(name=f'Equipment Exercise {i+1}:', value=f"Could not find an equipment-specific exercise for '{equipment_name}'.")




  embed.set_footer(text="Workout routine powered by ExerciseDB API")

  await message.channel.send(embed=embed)