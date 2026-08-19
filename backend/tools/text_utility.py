def text_utility(text: str, operation: str) -> int | str:
    """Perform basic text operations."""

    if operation == "word_count":
        return len(text.split())

    elif operation == "reverse":
        return text[::-1]

    elif operation == "uppercase":
        return text.upper()

    elif operation == "lowercase":
        return text.lower()

    else:
        return "Error: Unknown operation"