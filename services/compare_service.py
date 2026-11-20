"""
Document Comparison Service

Compares two document contexts.
"""

from llm.generator import ResponseGenerator
from llm.response_parser import ResponseParser
from prompts.compare_prompt import ComparePrompt


class CompareService:
    """
    Handles comparison between
    two document contexts.
    """

    def __init__(
        self,
        generator: ResponseGenerator,
        parser: ResponseParser,
    ):
        self.generator = generator
        self.parser = parser

    def compare(
        self,
        context_a: str,
        context_b: str,
    ) -> str:
        """
        Compare two documents.
        """

        prompt = ComparePrompt.build(
            context_a=context_a,
            context_b=context_b,
        )

        response = self.generator.generate_prompt(
            prompt
        )

        return self.parser.parse(
            response
        )