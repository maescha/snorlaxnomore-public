import discord
from utils.gemini import generated_custom_content
from utils.giphy import get_random_gif

def _gemini_response(user_input):
  prompt_text=f'Generate a Discord message using Markdown, reply as a fitness-obsessed Snorlax (important), do not exceed 2000 characters. Reply to: '
  full_prompt = prompt_text + user_input
  # print(full_prompt)
  return generated_custom_content(full_prompt)

async def command_chat(message):
  # removes the add text in the title
  message_content = message.content[len('chat '):].strip()
  # print(message_content)

  await message.channel.send(f"{_gemini_response(message_content)}")
  await message.channel.send(f"[gif]({get_random_gif('snorlax')})")