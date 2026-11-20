"""
Document Summary Service

Generates summaries for
uploaded documents.
"""

from retrieval.retriever import Retriever
from llm.generator import ResponseGenerator
from llm.response_parser import ResponseParser
from prompts.summary_prompt import SummaryPrompt


class SummaryService:
    """
    Handles document summarization.
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


    def summarize(
    self,
    query: str = "Summarize the document.",
    summary_type: str = "concise",
    top_k: int = 10,
) -> str:

    # Retrieve all indexed document chunks
        chunks = self.retriever.vector_search.metadata

        if not chunks:
            return "No document content found. Please upload a document first."

    # Combine the extracted text
        context = "\n\n".join(
            chunk.text
            for chunk in chunks
    )
        context = context[:5000]

        if not context.strip():
            return "No readable text was extracted from the document."

    # Build AI prompt
        prompt = SummaryPrompt.build(
            context=context,
            summary_type=summary_type,
    )

    # Generate summary using Llama 3
        response = self.generator.generate_prompt(prompt)

        return self.parser.parse(response)