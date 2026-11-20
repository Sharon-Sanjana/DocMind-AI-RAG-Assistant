"""
Embedding Model

Provides a wrapper around SentenceTransformer
for generating text embeddings.
"""

from typing import List

from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    Wrapper around SentenceTransformer.
    """

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
    ):
        """
        Initialize embedding model.

        """
        self.model_name = model_name
        self.model = SentenceTransformer(
            model_name
        )

    def encode(
        self,
        text: str,
    ) -> List[float]:
        """
        Convert text into an embedding vector.

        Args:
            text: Input text.

        Returns:
            Embedding vector.
        """

        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
        )

        return embedding.tolist()

    def batch_encode(
        self,
        texts: List[str],
    ) -> List[List[float]]:
        """
        Encode multiple texts.
        """

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
        )

        return embeddings.tolist()
    