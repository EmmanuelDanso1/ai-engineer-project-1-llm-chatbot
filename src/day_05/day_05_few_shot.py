from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

prompt = """
You are a review classifier.

I loved this movie. Great pacing and strong acting. → Positive
Not worth my time. The plot was confusing and boring. → Negative
Surprisingly good. I would watch it again. → Positive

The TRON movie is great and has a nice ending. →
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text.strip())
