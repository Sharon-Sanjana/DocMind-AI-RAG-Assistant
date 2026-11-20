"""
Chunk Overlap

Provides utilities for creating overlapping
text chunks.
"""

from typing import List


class ChunkOverlap:
    """
    Applies overlap between consecutive chunks.
    """

    @staticmethod
    def apply(
        chunks: List[str],
        overlap_size: int = 100,
    ) -> List[str]:
        """
        Apply overlap between chunks.

        Args:
            chunks: Original chunks.
            overlap_size: Number of characters
                to overlap.

        Returns:
            List of overlapping chunks.
        """

        if len(chunks) <= 1:
            return chunks

        overlapped_chunks = [
            chunks[0]
        ]

        for i in range(
            1,
            len(chunks),
        ):

            previous = chunks[i - 1]

            current = chunks[i]

            overlap = previous[
                -overlap_size:
            ]

            overlapped_chunks.append(
                overlap + current
            )

        return overlapped_chunks