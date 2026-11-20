"""
File Utilities

Provides reusable helper functions for
working with files and directories.
"""

import os
import uuid
from pathlib import Path

from config.settings import settings
from utils.exceptions import UnsupportedFileTypeError


def ensure_directory(directory: Path) -> None:
    """
    Create directory if it does not exist.
    """
    directory.mkdir(parents=True, exist_ok=True)


def file_exists(file_path: str) -> bool:
    """
    Check whether a file exists.
    """
    return Path(file_path).is_file()


def get_file_extension(file_path: str) -> str:
    """
    Return file extension in lowercase.
    """
    return Path(file_path).suffix.lower()


def get_file_size(file_path: str) -> int:
    """
    Return file size in bytes.
    """
    return os.path.getsize(file_path)


def validate_file_type(file_path: str) -> None:
    """
    Validate whether the uploaded file
    is supported.
    """
    extension = get_file_extension(file_path)

    if extension not in settings.SUPPORTED_EXTENSIONS:
        raise UnsupportedFileTypeError(
            f"Unsupported file type: {extension}"
        )


def generate_unique_filename(filename: str) -> str:
    """
    Generate a unique filename while
    preserving the original extension.
    """
    extension = Path(filename).suffix

    unique_name = uuid.uuid4().hex

    return f"{unique_name}{extension}"


def get_filename(file_path: str) -> str:
    """
    Return filename only.
    """
    return Path(file_path).name


def get_stem(file_path: str) -> str:
    """
    Return filename without extension.
    """
    return Path(file_path).stem