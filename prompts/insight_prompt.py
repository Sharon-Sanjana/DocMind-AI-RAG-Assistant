"""
Insight Prompt

Prompt template for generating
document insights.
"""


class InsightPrompt:
    """
    Builds prompts for document insights.
    """

    @staticmethod
    def build(
        context: str,
    ) -> str:
        """
        Build an insight generation prompt.
        """

        return f"""
You are an intelligent AI assistant.

Analyze the document carefully.

Provide:

- Key insights
- Important observations
- Trends
- Risks
- Opportunities
- Recommendations

Use ONLY the provided context.

Do not invent facts.

------------------------

Context:

{context}

------------------------

Insights:
"""