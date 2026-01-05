"""
Utility functions for estimating token usage.

NOTE:
Token counts are an approximation. Different models may tokenize text
slightly differently, but this estimate is sufficient for enforcing
context window limits safely.
"""

import tiktoken


def count_tokens(messages: list[dict[str, str]], model: str) -> int:
    """
    Estimate the number of tokens used by a list of chat messages.

    Each message is expected to be a dict with 'role' and 'content' keys.
    We count tokens from both fields.

    Args:
        messages: Chat history messages
        model: Model name (used to select tokenizer)

    Returns:
        Estimated token count
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        # Fallback for unknown models
        encoding = tiktoken.get_encoding("cl100k_base")

    total_tokens = 0
    for msg in messages:
        for value in msg.values():
            total_tokens += len(encoding.encode(value))

    return total_tokens
