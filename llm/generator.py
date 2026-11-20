"""
LLM Generator

Generates AI responses using
prepared prompts.
"""

from typing import List

from llm.ollama_client import OllamaClient
from models.chunk import Chunk
from prompts.qa_prompt import QAPrompt


class ResponseGenerator:
    """
    Generates responses using
    the language model.
    """

    def __init__(
        self,
        client: OllamaClient,
    ):
        self.client = client

    @staticmethod
    def build_context(
        chunks: List[Chunk],
    ) -> str:
        """
        Convert chunks into
        one context string.
        """

        return "\n\n".join(
            chunk.text
            for chunk in chunks
        )

    def generate_prompt(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a response from
        a prepared prompt.
        """

        return self.client.generate(
            prompt
        )

    def generate_qa(
        self,
        question: str,
        chunks: List[Chunk],
    ) -> str:
        """
        Generate a QA response.
        """

        context = self.build_context(
            chunks
        )

        prompt = QAPrompt.build(
            question=question,
            context=context,
        )

        return self.generate_prompt(
            prompt
        )