"""
Keyword Prompt

Prompt template for extracting
important keywords from documents.
"""

class KeywordPrompt:
    """
    Builds prompts for keyword extraction.
    """

    @staticmethod
    def build(
        context: str,
    ) -> str:
        """
        Build a keyword extraction prompt.
        """

        return f"""
You are an intelligent AI assistant.

Extract the most important keywords
from the document.

Requirements:

- Use ONLY the provided context.
- Do not invent information.
- Return 10–20 important keywords.
- Remove duplicate keywords.
- Return only a bullet list.

------------------------

Context:

{context}

------------------------

Keywords:
"""