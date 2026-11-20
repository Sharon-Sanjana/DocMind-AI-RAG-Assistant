"""
Document Chunker

Coordinates the chunking pipeline by applying
a chunking strategy, overlap, and creating
Chunk model objects.
"""

from typing import List

from models.document import Document
from models.chunk import Chunk

from chunking.strategies import ChunkStrategy
from chunking.overlap import ChunkOverlap


class DocumentChunker:
    """
    Creates Chunk objects from a Document.
    """

    def __init__(
        self,
        strategy: ChunkStrategy,
        overlap_size: int = 100,
    ):
        self.strategy = strategy
        self.overlap_size = overlap_size

    def chunk(
        self,
        document: Document,
    ) -> List[Chunk]:
        """
        Split a document into Chunk objects.
        """

        # Step 1: Split text
        raw_chunks = self.strategy.split(
            document.text
        )

        # Step 2: Apply overlap
        raw_chunks = ChunkOverlap.apply(
            raw_chunks,
            self.overlap_size,
        )

        # Step 3: Create Chunk objects
        chunks = []

        total_chunks = len(raw_chunks)

        for index, text in enumerate(
            raw_chunks,
            start=1,
        ):

            chunk = Chunk(
                document_id=document.document_id,
                text=text,
                chunk_index=index,
            )

            chunks.append(chunk)

        return chunks