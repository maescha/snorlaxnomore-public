import discord

async def command_hello(message):
    await message.channel.send(f'# :wave: Hello {message.author.display_name}')
    await message.channel.send(f'-# **It\'s time to get fit! :person_lifting_weights: **')