"""
Helper Utilities

General-purpose helper functions used across
the DocMind-AI application.
"""

import re
import uuid
from datetime import datetime


def generate_timestamp() -> str:
    """
    Return the current timestamp in ISO format.
    """
    return datetime.now().isoformat()


def normalize_text(text: str) -> str:
    """
    Remove extra whitespace from text.
    """
    return re.sub(r"\s+", " ", text).strip()


def truncate_text(text: str, max_length: int = 100) -> str:
    """
    Truncate long text for logging or previews.
    """
    if len(text) <= max_length:
        return text

    return text[:max_length] + "..."


def bytes_to_mb(size: int) -> float:
    """
    Convert bytes into megabytes.
    """
    return round(size / (1024 * 1024), 2)


def is_valid_uuid(value: str) -> bool:
    """
    Check whether a string is a valid UUID.
    """
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False


def safe_get(dictionary: dict, key, default=None):
    """
    Safely retrieve a value from a dictionary.
    """
    return dictionary.get(key, default)


def remove_empty_lines(text: str) -> str:
    """
    Remove empty lines from text.
    """
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    return "\n".join(lines)