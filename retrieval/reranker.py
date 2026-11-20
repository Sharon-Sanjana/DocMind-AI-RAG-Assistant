"""
Reranker

Ranks retrieved chunks based on relevance.
"""

from typing import List

from models.chunk import Chunk


class Reranker:
    """
    Reranks retrieved chunks.
    """

    def rerank(
        self,
        question: str,
        chunks: List[Chunk],
        top_k: int = 5,
    ) -> List[Chunk]:
        """
        Rerank chunks using a simple relevance score.

        Current implementation:
        - Scores chunks by keyword overlap.
        - Returns the top_k chunks.

        Future implementation:
        - Replace with CrossEncoder.
        """

        question_words = set(
            question.lower().split()
        )

        scored_chunks = []

        for chunk in chunks:

            chunk_words = set(
                chunk.text.lower().split()
            )

            score = len(
                question_words.intersection(
                    chunk_words
                )
            )

            scored_chunks.append(
                (
                    score,
                    chunk,
                )
            )

        scored_chunks.sort(
            key=lambda x: x[0],
            reverse=True,
        )

        return [
            chunk
            for _, chunk in scored_chunks[:top_k]
        ]