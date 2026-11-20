"""
Chat UI

Displays the chat interface
and communicates with the
Question Answering service.
"""

import streamlit as st

from ui.components import UIComponents


class ChatUI:
    """
    Chat interface.
    """

    @staticmethod
    def render(
        qa_service,
        settings,
    ):
        """
        Render chat interface.
        """

        st.subheader(
            "💬 Chat with your Documents"
        )

        if not UIComponents.require_documents():
            return

        # Display previous messages
        for message in st.session_state.messages:

            with st.chat_message(
                message["role"]
            ):

                st.markdown(
                    message["content"]
                )

        # User input
        question = st.chat_input(
            "Ask a question about your documents..."
        )

        question = (question or "").strip()
       
        if not question:
            return

        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        with st.chat_message("user"):

            st.markdown(question)

        # Generate AI response
        with st.chat_message("assistant"):

            with UIComponents.loading(
                "Searching documents and generating answer..."
            ):

                try:

                    answer = qa_service.answer(
                    question=question,
                    top_k=settings["top_k"],
                    )

                except Exception as error:

                    answer = (
                    "❌ An error occurred while "
                    "generating the response.\n\n"
                    f"{error}"
                )

                st.markdown(answer)

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )