import discord
import csv

from utils.giphy import get_random_gif

def __count_lines(file_path):
  with open(file_path, 'r') as file:
    lines = file.readlines()
    return len(lines)


async def command_add(message):
  # removes the add text in the title
  message_content = message.content[len('add '):].strip()

  default_playlist_file = 'playlist.csv'

  with open(default_playlist_file, 'a', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow([message_content])

  embed = discord.Embed(title='Happy to see you keep the dream alive!', description=f':woman_cartwheeling:  {message.author.display_name} added to the workout playlist and is staying fit with Snorlax')
  embed.add_field(name='Lets go! :raised_hands: ', value=f'Your [video]({message_content}) is now part of the playlist', inline=False)
  embed.set_footer(text=f'Playlist is currently at {(__count_lines(default_playlist_file))} videos')
  embed.set_image(url=get_random_gif('happy'))

  await message.channel.send(embed=embed)