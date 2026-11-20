"""
Question Answering Service

Coordinates retrieval, generation,
and response parsing.
"""

from retrieval.retriever import Retriever
from llm.generator import ResponseGenerator
from llm.response_parser import ResponseParser


class QAService:
    """
    Handles document question answering.
    """

    def __init__(
        self,
        retriever: Retriever,
        generator: ResponseGenerator,
        parser: ResponseParser,
    ):
        self.retriever = retriever
        self.generator = generator
        self.parser = parser

    def answer(
        self,
        question: str,
        top_k: int = 5,
    ) -> str:
        """
        Generate an answer for
        the user's question.
        """

        chunks = self.retriever.retrieve(
            query=question,
            top_k=top_k,
        )

        response = self.generator.generate_qa(
            question=question,
            chunks=chunks,
        )

        return self.parser.parse(
            response
        )