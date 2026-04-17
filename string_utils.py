"""String utility functions."""


def reverse(s: str) -> str:
    """Return the reversed string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Return True if s reads the same forwards and backwards (case-insensitive)."""
    normalized = s.lower().replace(" ", "")
    return normalized == normalized[::-1]


def word_count(s: str) -> int:
    """Return the number of words in s."""
    return len(s.split())


def capitalize_words(s: str) -> str:
    """Return s with each word capitalized."""
    return " ".join(word.capitalize() for word in s.split())
