"""
Keyword Extraction Service

Extracts important keywords
from uploaded documents.
"""

from retrieval.retriever import Retriever
from llm.generator import ResponseGenerator
from llm.response_parser import ResponseParser
from prompts.keyword_prompt import KeywordPrompt

class KeywordService:
    """
    Handles keyword extraction.
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

    def extract(
        self,
        query: str = "Important keywords",
        top_k: int = 10,
    ) -> str:
        """
        Extract document keywords.
        """

        chunks = self.retriever.retrieve(
            query=query,
            top_k=top_k,
        )

        context = self.generator.build_context(
            chunks
        )

        prompt = KeywordPrompt.build(
            context=context
        )

        response = self.generator.generate_prompt(
            prompt
        )

        return self.parser.parse(
            response
        )