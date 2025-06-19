import discord
import requests
import json

import random

from utils.giphy import get_random_gif

url = 'https://exercisedb-api.vercel.app/api/v1/equipments/body%20weight/exercises'

def __get_random_exercise_no_equipment():
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
      target_Muscles = random_exercise.get('targetMuscles')

      results_data.append({
        'name': name,
        'instructions': instructions,
        'target_Muscles': target_Muscles
      })

      return results_data
  else:
      return 'No exercises found'


async def command_randExercise(message):
  await message.channel.send('# DID I HEAR RIGHT :eyes:')
  await message.channel.send('-# someone said **the** word!')
  workout_details = __get_random_exercise_no_equipment()

  if not workout_details:
    await message.channel.send('Sorry, I\'m blanking out on spontaneous workout ideas')
    return

  response_message = ''

  details = workout_details[0]

  name = details.get('name')
  instructions = details.get('instructions')
  target_Muscles = details.get('target_Muscles')

  embed_title = f'I think you would benefit from doing some **{name}s** \n'

  if instructions:
    response_message += "**Instructions:**\n"
    cleaned_instructions = []

    for step in instructions:
      if step.startswith("Step:") and ' ' in step:
        cleaned_instructions.append(step.split(' ', 1)[1])
      else:
        cleaned_instructions.append(step)

    response_message += "\n".join([f"- {step_clean}" for step_clean in cleaned_instructions]) + "\n"

    embed = discord.Embed(title=embed_title, description=response_message)
    embed.set_thumbnail(url=get_random_gif('exercise'))
    await message.channel.send(embed=embed)

    if target_Muscles:
      await message.channel.send(f"You do this enough times, you\'ll be sure to improve your **{', '.join(target_Muscles)}**!\n")