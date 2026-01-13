import os
from dotenv import load_dotenv

load_dotenv()

P1_MODEL = os.getenv("P1_MODEL")
P1_TEMPERATURE = float(os.getenv("P1_TEMPERATURE"))
P1_MAX_TOKENS = int(os.getenv("P1_MAX_TOKENS"))

EXERCISE_MAX_CONTEXT_TOKENS = 4096
