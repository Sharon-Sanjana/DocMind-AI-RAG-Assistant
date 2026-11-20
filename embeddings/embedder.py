"""
Embedder

Generates embeddings for Chunk objects.
"""

from typing import List

from embeddings.embedding_model import EmbeddingModel
from models.chunk import Chunk


class Embedder:
    """
    Generates embeddings for document chunks.
    """

    def __init__(self, embedding_model: EmbeddingModel):
        self.embedding_model = embedding_model

    def embed_chunk(self, chunk: Chunk) -> Chunk:
        """
        Generate embedding for a single chunk.
        """

        chunk.embedding = self.embedding_model.encode(
            chunk.text
        )

        return chunk

    def embed_chunks(
        self,
        chunks: List[Chunk],
    ) -> List[Chunk]:
        """
        Generate embeddings for multiple chunks.
        """

        texts = [
            chunk.text
            for chunk in chunks
        ]

        embeddings = (
            self.embedding_model.batch_encode(
                texts
            )
        )

        for chunk, embedding in zip(
            chunks,
            embeddings,
        ):
            chunk.embedding = embedding

        return chunks