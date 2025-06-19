import discord

from utils.equipment_muscles_options import _get_userinput_return_workout_options
from utils.giphy import get_random_gif

async def return_options_msging(message):
  embed = discord.Embed(title='Let\'s set up that routine!', description='Now that you have the available options, lets customize something for you!')
  embed.add_field(name="Equipment-Specific", value="To create an equipment-specific routine, type `!eq [equipment name]` \n For example, `!eq upper body ergometer`")
  embed.add_field(name="Targetting Specific Muscle Group", value="To create a muscle-targetted routine, type `!musc [muscle name]` \n For example, `!musc cardiovascular system`")
  embed.set_image(url=get_random_gif('excited dog excercise'))
  embed.set_footer(text='Love this for you (,,♡ᵕ♡,,) !')

  await _get_userinput_return_workout_options(message)
  await message.channel.send(embed=embed)