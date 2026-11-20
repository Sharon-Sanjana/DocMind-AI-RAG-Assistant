"""
Timer Utility

Provides a reusable context manager for measuring
execution time of code blocks.
"""

import time
from contextlib import ContextDecorator

from utils.logger import get_logger

logger = get_logger(__name__)


class Timer(ContextDecorator):
    """
    Context manager for measuring execution time.

    Example:
        with Timer("Embedding Generation"):
            generate_embeddings()
    """

    def __init__(self, operation: str):
        self.operation = operation
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None

    def __enter__(self):
        """
        Start the timer.
        """
        self.start_time = time.perf_counter()

        logger.info(
            "Started: %s",
            self.operation
        )

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Stop the timer and log execution time.
        """
        self.end_time = time.perf_counter()

        self.elapsed_time = (
            self.end_time - self.start_time
        )

        logger.info(
            "%s completed in %.4f seconds",
            self.operation,
            self.elapsed_time,
        )

        return False

    @property
    def seconds(self):
        """
        Returns elapsed time in seconds.
        """
        return self.elapsed_time