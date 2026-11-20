"""
FAISS Vector Store

Stores and searches document embeddings.
"""

from typing import List

import faiss
import numpy as np


class FAISSStore:
    """
    Handles vector storage and similarity search.
    """

    def __init__(
        self,
        dimension: int,
    ):
        """
        Initialize FAISS index.
        """

        self.dimension = dimension

        self.index = faiss.IndexFlatL2(
            dimension
        )

    def add(
        self,
        embeddings: List[List[float]],
    ) -> None:
        """
        Add embeddings to the index.
        """

        vectors = np.array(
            embeddings,
            dtype=np.float32,
        )

        self.index.add(vectors)

    def search(
        self,
        query_embedding: List[float],
        k: int = 5,
    ):
        """
        Search nearest vectors.
        """

        query = np.array(
            [query_embedding],
            dtype=np.float32,
        )

        distances, indices = self.index.search(
            query,
            k,
        )

        return distances[0], indices[0]

    def size(
        self,
    ) -> int:
        """
        Return number of stored vectors.
        """

        return self.index.ntotal