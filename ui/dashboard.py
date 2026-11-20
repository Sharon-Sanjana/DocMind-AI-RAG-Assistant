"""
Dashboard UI

Displays application overview.
"""

import streamlit as st


class Dashboard:
    """
    Dashboard component.
    """

    @staticmethod
    def render():
        """
        Render dashboard.
        """

        st.title("📄 DocMind-AI")

        st.markdown(
            """
Enterprise-grade Retrieval-Augmented Generation (RAG) Platform

Upload documents, ask questions, generate summaries,
compare documents, extract keywords, and discover insights.
"""
        )

        st.divider()

        uploaded_documents = len(
            st.session_state.uploaded_documents
        )

        total_messages = len(
            st.session_state.messages
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Uploaded Documents",
                uploaded_documents,
            )

        with col2:

            st.metric(
                "Chat Messages",
                total_messages,
            )

        st.divider()

        st.subheader("Available AI Features")

        features = [

            "💬 Question Answering",

            "📝 Document Summarization",

            "📄 Document Comparison",

            "🔑 Keyword Extraction",

            "💡 Insight Generation",
        ]

        for feature in features:

            st.markdown(f"✅ {feature}")

        st.divider()

        if uploaded_documents == 0:

            st.info(
        "Upload one or more documents to begin."
    )

        else:

            st.success(
        "Documents are indexed and ready for AI tasks."
    )