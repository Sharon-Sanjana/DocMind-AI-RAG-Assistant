"""
Vector Search

Performs semantic search
using FAISS.
"""

from typing import List

from models.chunk import Chunk
from vectorstore.faiss_store import FAISSStore


class VectorSearch:
    """
    Performs similarity search.
    """

    def __init__(
        self,
        faiss_store: FAISSStore,
        metadata: List[Chunk],
    ):
        self.faiss_store = faiss_store
        self.metadata = metadata

    def search(
        self,
        query_embedding: List[float],
        top_k: int = 5,
    ) -> List[Chunk]:
        """
        Retrieve the most similar chunks.
        """

        _, indices = self.faiss_store.search(
            query_embedding,
            top_k,
        )

        results = []

        for index in indices:

            if (
                index == -1
                or index >= len(self.metadata)
            ):
                continue

            results.append(
                self.metadata[index]
            )

        return results