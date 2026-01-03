import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Import env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=GEMINI_API_KEY)
chat = client.chats.create(model="gemini-2.5-flash")

while True:
    user_input = input("You: ")

    # ignore empty input (if user hits Enter, reprompt without calling the API)
    if not user_input:
        continue
    # exit when the user types any of: quit, exit, /quit
    if user_input in ("exit", "quit"):
        print("Goodbye")
        break
    # Gets chat history
    elif user_input == "history":
        print(chat.get_history())
    else:
        response = chat.send_message(user_input)
        print("AI:", response.text)