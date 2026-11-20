"""
Chunking Strategies

Defines chunking strategies used by the
Chunker.
"""

from abc import ABC, abstractmethod
from typing import List


class ChunkStrategy(ABC):
    """
    Abstract base class for chunking strategies.
    """

    @abstractmethod
    def split(self, text: str) -> List[str]:
        """
        Split text into chunks.
        """
        pass


class FixedSizeChunkStrategy(ChunkStrategy):
    """
    Splits text into fixed-size chunks.
    """

    def __init__(self, chunk_size: int = 500):
        self.chunk_size = chunk_size

    def split(self, text: str) -> List[str]:

        chunks = []

        for i in range(
            0,
            len(text),
            self.chunk_size,
        ):

            chunks.append(
                text[i:i + self.chunk_size]
            )

        return chunks


class ParagraphChunkStrategy(ChunkStrategy):
    """
    Splits text by paragraphs.
    """

    def split(self, text: str) -> List[str]:

        paragraphs = text.split("\n\n")

        return [
            p.strip()
            for p in paragraphs
            if p.strip()
        ]