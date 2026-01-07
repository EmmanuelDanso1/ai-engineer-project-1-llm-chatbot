from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

question = (
    "A coffee shop sells cups for $3 each and muffins for $2 each. "
    "If you buy 4 cups and 5 muffins, how much do you spend in total?"
)

# ZERO SHOT
zero_shot = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=question
)

# STEP BY STEP
step_by_step = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=(
        "Explain your reasoning step-by-step, then give the final answer.\n\n"
        + question
    )
)

print("=== ZERO SHOT ===")
print(zero_shot.text.strip())

print("\n=== STEP BY STEP ===")
print(step_by_step.text.strip())
