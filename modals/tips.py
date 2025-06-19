import discord
import json

from utils.gemini import generated_tip_content

async def modal_tips(interaction: discord.Interaction):
  modal = tips_form()
  await interaction.response.send_modal(modal)

class tips_form(discord.ui.Modal):
  def __init__(self):
    super().__init__(title="Health Starts with Self-Awareness")

  fitness_goal = discord.ui.TextInput(label="Describe your general fitness/lifestyle goal", style=discord.TextStyle.paragraph, placeholder="Improve overall health, energy levels, and sleep quality", required= True, max_length= 500)
  fitness_level = discord.ui.TextInput(label="What is your current fitness level", style=discord.TextStyle.long, placeholder="Current fitness: strength, endurance, flexibility, and limitations", required= True, max_length= 500)
  lifestyle = discord.ui.TextInput(label="What is your lifestyle like?", style=discord.TextStyle.long, placeholder="Time commitments, equipment access (gym/home), and preferences?", required= True, max_length= 500)

  async def on_submit(self, interaction: discord.Interaction):
    goal_text = self.fitness_goal.value.strip()
    level_text = self.fitness_level.value.strip()
    lifestyle_text = self.lifestyle.value.strip()

    print(f"Modal Submitted by {interaction.user.display_name}")
    submitted_data = {
      # "username": interaction.user.name,
      "fitness_goal": goal_text,
      "fitness_level": level_text,
      "lifestyle": lifestyle_text
    }

    json_data = json.dumps(submitted_data, indent=4)
    # print(json_data)

    await interaction.response.send_message("Thank you for sharing, Snorlax is thinking up some tips for you")
    await interaction.message.channel.send(f"Hi **{interaction.user.display_name}** :wave:! {generated_tip_content(json_data)}")

  async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
    print(f"Error submitting modal for {interaction.user.display_name}: {error}")
    await interaction.response.send_message("An error occurred while processing your form. Please try again later.", ephemeral=True)

class tip_modal_view(discord.ui.View):
  def __init__(self, *, timeout = 180):
    super().__init__(timeout=timeout)

  @discord.ui.button(label="Change my life Snorlax!", style=discord.ButtonStyle.primary, emoji="✨")
  async def open_modal_button(self, interaction: discord.Interaction, button: discord.ui.Button):
    print(f"Button clicked by {interaction.user.display_name}. Opening modal ...")
    await modal_tips(interaction)