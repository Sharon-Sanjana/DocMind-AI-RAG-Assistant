"""
Document Insight Service

Generates insights from
uploaded documents.
"""

from retrieval.retriever import Retriever
from llm.generator import ResponseGenerator
from llm.response_parser import ResponseParser
from prompts.insight_prompt import InsightPrompt



class InsightService:
    """
    Generates insights from documents.
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

    def generate(
        self,
        query: str = "Generate insights",
        top_k: int = 10,
    ) -> str:
        """
        Generate document insights.
        """

        chunks = self.retriever.retrieve(
            query=query,
            top_k=top_k,
        )

        context = self.generator.build_context(
            chunks
        )

        prompt = InsightPrompt.build(
           context=context
        )

 

        response = self.generator.generate_prompt(
            prompt
        )

        return self.parser.parse(
            response
        )