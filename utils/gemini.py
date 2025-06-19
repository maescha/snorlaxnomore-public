from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
gemini_API_key= os.getenv('GEMINIKEY')

client = genai.Client(api_key=gemini_API_key)

def generated_tip_content(user_input):
  response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=f'Generate a helpful and meaningful response that is around 1000 characters, do not exceed 2000 characters, use Markdown in output as this is for a Discord message. Recommend tips to meet fitness/health/wellness goal according to this provided information: {user_input} and sound encouraging'
  )

  return response.text

def generated_custom_content(user_input):
  response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=f'{user_input}'
  )

  return response.text