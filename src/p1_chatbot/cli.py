import os
from dotenv import load_dotenv
from google import genai

from .tokens import count_tokens
from .prompts import SYSTEM_PROMPT

load_dotenv()

# ======================
# CONFIG
# ======================
MODEL_NAME = "gemini-2.5-flash"

EXERCISE_MAX_CONTEXT_TOKENS = 4096
RESERVED_OUTPUT_TOKENS = 500
TRUNCATE_THRESHOLD_TOKENS = 3500

# NB:
# Gemini chat sessions do not currently support temperature control.
# We define TEMPERATURE = 0.1 to document stable generation intent,
TEMPERATURE = 0.1


# coT = Chain of Thought
cot_mode = False

# ======================
# CLIENT SETUP
# ======================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

chat = client.chats.create(model=MODEL_NAME)


# Maintain our own message history
messages: list[dict[str, str]] = [{"role": "system", "content": SYSTEM_PROMPT}]

# ======================
# MAIN LOOP
# ======================
while True:
    user_input = input("You: ")

    # if user press enter without typing anything
    if not user_input:
        continue

    # If user type exit or quit
    if user_input in ("exit", "quit", "/quit"):
        print("Goodbye")
        break

    

    # Get history
    if user_input == "history":
        print(messages)
        continue

    # Chain of thoughts enabled
    if user_input.lower() == "/cot":
        cot_mode = True
        print("[mode] CoT enabled for next turn.")
        continue


    # Add user message
    # messages.append({"role": "user", "content": user_input})

    if cot_mode:
        user_input = (
            "Explain your reasoning step-by-step, then give the final answer.\n\n"
            + user_input
        )

    messages.append({"role": "user", "content": user_input})


    # ======================
    # TOKEN COUNTING
    # ======================
    input_tokens_estimate = count_tokens(messages, MODEL_NAME)
    print(f"Tokens (estimated input): {input_tokens_estimate}")

    # ======================
    # SYSTEM PROMPT
    # ======================
    while (
        input_tokens_estimate + RESERVED_OUTPUT_TOKENS
        > EXERCISE_MAX_CONTEXT_TOKENS
    ):
        # Never remove system prompt
        if len(messages) > 2 and messages[0]["role"] == "system":
            # Remove oldest user+assistant pair AFTER system prompt
            messages.pop(1)
            messages.pop(1)
            print("[context] Truncated oldest messages to fit token budget.")
        elif len(messages) > 1:
            messages.pop(1)
            print("[context] Truncated malformed message.")
        else:
            break

        input_tokens_estimate = count_tokens(messages, MODEL_NAME)

    # ======================
    # API CALL
    # ======================
    response = chat.send_message(user_input)


    assistant_reply = response.text
    print("AI:", assistant_reply)

    messages.append({"role": "assistant", "content": assistant_reply})

    if cot_mode:
        cot_mode = False
        print("[mode] CoT disabled.")
