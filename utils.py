"""Simple utility functions."""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 0


def factorial(n: int) -> int:
    """Return the factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)
