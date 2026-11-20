"""
Extractor Prompt

Prompt template for extracting
structured information from documents.
"""


class ExtractorPrompt:
    """
    Builds prompts for extracting
    important information.
    """

    @staticmethod
    def build(
        context: str,
    ) -> str:
        """
        Build an extraction prompt.
        """

        return f"""
You are an intelligent AI assistant.

Extract all important information
from the provided document.

Use ONLY the information found
inside the context.

If a field is unavailable,
write:

Not Available

Return the information
using the following format.

------------------------

Title:

People:

Organizations:

Dates:

Locations:

Email Addresses:

Phone Numbers:

Important Keywords:

Summary:

------------------------

Context:

{context}

------------------------

Extraction:
"""