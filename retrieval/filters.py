"""
Retrieval Filters

Filters retrieved chunks
based on metadata.
"""

from typing import List, Optional

from models.chunk import Chunk


class RetrievalFilter:
    """
    Applies metadata filters
    to retrieved chunks.
    """

    def filter_by_document(
        self,
        chunks: List[Chunk],
        document_id: str,
    ) -> List[Chunk]:
        """
        Return chunks belonging to one document.
        """

        return [
            chunk
            for chunk in chunks
            if chunk.document_id == document_id
        ]

    def filter_by_metadata(
        self,
        chunks: List[Chunk],
        key: str,
        value,
    ) -> List[Chunk]:
        """
        Filter using metadata key/value.
        """

        return [
            chunk
            for chunk in chunks
            if chunk.metadata.get(key) == value
        ]

    def filter_by_chunk_index(
        self,
        chunks: List[Chunk],
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> List[Chunk]:
        """
        Filter chunks by chunk index range.
        """

        filtered = []

        for chunk in chunks:

            if start is not None and chunk.chunk_index < start:
                continue

            if end is not None and chunk.chunk_index > end:
                continue

            filtered.append(chunk)

        return filtered