import discord
from utils.gemini import generated_custom_content
from utils.giphy import get_random_gif

def _gemini_prompt(prompt):
  prompt_text='Generate a short encouraging message using Markdown and emojis in response to the user indicating that they had trouble completing the fitness exercuse due to '
  full_prompt = prompt_text + prompt
  return generated_custom_content(full_prompt)

class footer_buttons(discord.ui.View):
  def __init__(self):
        super().__init__()

  ## logging for snorlax leveling
  @discord.ui.button(label="Log", style=discord.ButtonStyle.blurple, emoji="✍️")
  async def button_logging_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
    ## to hide text
    await interaction.response.send_message(f"[good job]({get_random_gif('good job')})")
    await interaction.followup.send("Logging it now (Logging functionality coming soon)", ephemeral=True)

  ##gemini
  @discord.ui.button(label="No motivation", style=discord.ButtonStyle.grey, emoji="😔")
  async def button_one_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(f"{_gemini_prompt('no motivation')}", ephemeral=True)

  @discord.ui.button(label="This is too much", style=discord.ButtonStyle.grey, emoji="🫨")
  async def button_three_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(f"{_gemini_prompt('exercise being too much for them. Encourage them to call !play for a random exercise routine that they can go at their own pace with, a little is a lot')}", ephemeral=True)
