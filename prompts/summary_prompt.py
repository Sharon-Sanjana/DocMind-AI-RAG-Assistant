"""
Summary Prompt

Prompt template for document summarization.
"""


class SummaryPrompt:
    """
    Builds prompts for document summaries.
    """

    @staticmethod
    def build(
        context: str,
        summary_type: str = "concise",
    ) -> str:
        """
        Build a summarization prompt.

        summary_type:
            - concise
            - detailed
            - bullet
        """

        if summary_type == "bullet":

            instruction = (
                "Summarize the document "
                "using concise bullet points."
            )

        elif summary_type == "detailed":

            instruction = (
                "Provide a detailed summary "
                "covering all major ideas."
            )

        else:

            instruction = (
                "Provide a concise summary "
                "highlighting the key points."
            )

        return f"""
You are an intelligent AI assistant.

Summarize ONLY the information
contained inside the context.

Do not invent facts.

{instruction}

------------------------

Context:

{context}

------------------------

Summary:
"""