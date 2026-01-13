import time
from typing import List, Dict, Tuple, Optional
from google import genai
from google.api_core.exceptions import (
    GoogleAPIError,
    ResourceExhausted,
    Unauthorized,
    ServiceUnavailable,
)

from .config import P1_MODEL, P1_MAX_TOKENS


def create_chat_completion(
    chat,
    user_input: str,
) -> Tuple[str, Optional[int], Optional[int]]:
    """
    Sends a message to Gemini with retries and error handling.

    Returns:
        assistant_text, prompt_tokens, completion_tokens
    """

    retries = 5
    backoff = 1

    for attempt in range(1, retries + 1):
        try:
            response = chat.send_message(user_input)

            text = response.text
            usage = getattr(response, "usage", None)

            if usage:
                return text, usage.prompt_tokens, usage.completion_tokens

            # Gemini fallback: token usage not always available
            return text, None, None

        except Unauthorized:
            print(
                "[error] Authentication failed. "
                "Please set GEMINI_API_KEY in your .env file."
            )
            return "", None, None

        except ResourceExhausted:
            if attempt < retries:
                print(
                    f"[rate limit] Retry {attempt}/{retries} "
                    f"— waiting {backoff}s..."
                )
                time.sleep(backoff)
                backoff *= 2
            else:
                print("[error] Rate limit exceeded. Try again later.")
                return "", None, None

        except (ServiceUnavailable, GoogleAPIError) as e:
            if attempt < retries:
                print(
                    f"[network] Temporary error ({e}). "
                    f"Retrying in {backoff}s..."
                )
                time.sleep(backoff)
                backoff *= 2
            else:
                print("[error] Network failure. Please check your connection.")
                return "", None, None
