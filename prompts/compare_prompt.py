"""
Compare Prompt

Prompt template for comparing
two documents.
"""


class ComparePrompt:
    """
    Builds prompts for comparing documents.
    """

    @staticmethod
    def build(
        context_a: str,
        context_b: str,
    ) -> str:
        """
        Build a comparison prompt.
        """

        return f"""
You are an intelligent AI assistant.

Compare the two document contexts.

Identify:

- Similarities
- Differences
- Important observations

Use ONLY the information
provided below.

Do not invent information.

------------------------

Document A

{context_a}

------------------------

Document B

{context_b}

------------------------

Provide the comparison using
the following format:

Similarities:
- ...

Differences:
- ...

Conclusion:
...
"""