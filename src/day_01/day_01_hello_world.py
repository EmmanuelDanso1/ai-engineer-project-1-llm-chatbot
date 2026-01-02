from dotenv import load_dotenv
from openai import OpenAI
import os
import sys

from google import genai

load_dotenv()

# Import env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Explain the difference between an AI Engineer and a Software Engineer in one sentence."
)
print(response.text)