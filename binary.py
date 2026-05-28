def to_binary(n: int) -> str:
    """Convert number 0-100 to binary string."""

    if not isinstance(n, int):
        raise ValueError("Input must be integer")

    if n < 0 or n > 100:
        raise ValueError("Out of range (0-100)")

    return bin(n)[2:]
