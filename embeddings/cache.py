"""
Embedding Cache

Caches embeddings to avoid
recomputing identical text.
"""

import hashlib
from typing import Dict, List, Optional


class EmbeddingCache:
    """
    In-memory embedding cache.
    """

    def __init__(self):

        self.cache: Dict[
            str,
            List[float]
        ] = {}

    def _hash(
        self,
        text: str,
    ) -> str:
        """
        Generate unique hash.
        """

        return hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

    def get(
        self,
        text: str,
    ) -> Optional[List[float]]:
        """
        Retrieve cached embedding.
        """

        key = self._hash(text)

        return self.cache.get(key)

    def set(
        self,
        text: str,
        embedding: List[float],
    ) -> None:
        """
        Store embedding.
        """

        key = self._hash(text)

        self.cache[key] = embedding

    def exists(
        self,
        text: str,
    ) -> bool:
        """
        Check cache.
        """

        key = self._hash(text)

        return key in self.cache

    def clear(
        self,
    ) -> None:
        """
        Remove all cached embeddings.
        """

        self.cache.clear()

    def size(
        self,
    ) -> int:
        """
        Number of cached items.
        """

        return len(self.cache)