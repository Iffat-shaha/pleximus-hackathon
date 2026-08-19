def calculator(a: float, b: float, operation: str) -> float | str:
    """Perform basic arithmetic operations."""

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

    else:
        return "Error: Unknown operation"