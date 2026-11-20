"""
Question Answer Prompt

Prompt template used for
document question answering.
"""


class QAPrompt:
    """
    Builds prompts for question answering.
    """

    @staticmethod
    def build(
        question: str,
        context: str,
    ) -> str:
        """
        Build the QA prompt.
        """

        return f"""
You are an intelligent AI assistant.

Answer the user's question ONLY
using the information contained
inside the context.

If the answer cannot be found
inside the context, reply:

"I couldn't find that information
in the uploaded documents."

Do not make assumptions.

------------------------

Context:

{context}

------------------------

Question:

{question}

------------------------

Answer:
"""