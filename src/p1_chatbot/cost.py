"""
Cost estimation utilities for LLM usage.
"""

MODEL_PRICING_USD_PER_1K: dict[str, tuple[float, float]] = {
    # model_name: (input_cost_per_1k, output_cost_per_1k)
    "gemini-2.5-flash": (0.00035, 0.00053),
}


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """
    Estimate the USD cost of an API call.

    Args:
        model: Model name used for the request
        input_tokens: Number of prompt tokens
        output_tokens: Number of completion tokens

    Returns:
        Estimated cost in USD
    """
    if model not in MODEL_PRICING_USD_PER_1K:
        raise ValueError(f"Unknown model pricing for: {model}")

    input_price, output_price = MODEL_PRICING_USD_PER_1K[model]

    input_cost = (input_tokens / 1000) * input_price
    output_cost = (output_tokens / 1000) * output_price

    return input_cost + output_cost
