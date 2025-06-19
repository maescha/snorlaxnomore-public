import discord
import logging
import os
from dotenv import load_dotenv

from commands.hello import command_hello
from commands.randExercise import command_randExercise
from commands.addVid import command_add
from commands.playVid import command_play
from commands.opt import return_options_msging
from commands.equipment_routine import specialized_eq_routine
from commands.muscle_routine import specialized_musc_routine
from commands.trainer import command_chat

from modals.tips import tip_modal_view

from utils.footer import footer_buttons

load_dotenv()
bot_token= os.getenv('DISCORDBOTTOKEN')

## basic logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

## set command prefix and refractor
def is_command(message, command):
  return message.content.startswith(f"!{command}")

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  ## commands
  async def on_message(self, message):
    if message.author == self.user:
      return

    randExercise_triggering_keywords = ('workout', 'working out', 'work out', 'fit', 'exercise', 'lazy', 'training', 'stronk', 'muscles', 'strong')

    if is_command(message, 'chat'):
      await command_chat(message)
    elif any(keyword in message.content.lower() for keyword in randExercise_triggering_keywords):
      await command_randExercise(message)
      await message.channel.send("-# ٩>ᴗ<)و Did you do it? Let's log that :partying_face: ! Or did you have trouble getting started? :worried: (don't worry it's just between you and me)", view=footer_buttons())
    elif is_command(message, 'add'):
      await command_add(message)
    elif is_command(message, 'play'):
      await command_play(message)
      await message.channel.send("-# Let's log that :partying_face: Or did you have trouble getting started? :worried: (don't worry it's just between you and me)", view=footer_buttons())
    elif is_command(message, 'tip'):
      await message.channel.send("Click the button below to request specialized fitness tips from Snorlax:", view=tip_modal_view())
    elif is_command(message, 'opt'):
      await return_options_msging(message)
    elif is_command(message, 'eq'):
      await specialized_eq_routine(message)
      await message.channel.send(" ", view=footer_buttons())
    elif is_command(message, 'musc'):
      await specialized_musc_routine(message)
      await message.channel.send(" ", view=footer_buttons())
    elif is_command(message, 'hello'):
      await command_hello(message)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(bot_token, log_handler=handler, log_level=logging.DEBUG)
