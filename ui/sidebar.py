"""
Sidebar UI

Provides navigation and
application settings.
"""

import streamlit as st


class Sidebar:
    """
    Sidebar component.
    """

    @staticmethod
    def render():
        """
        Render sidebar.
        """

        with st.sidebar:

            st.title("📄 DocMind-AI")

            st.divider()

            task = st.selectbox(
                "AI Task",
                (
                    "Question Answering",
                    "Summary",
                    "Compare Documents",
                    "Keyword Extraction",
                    "Insights",
                ),
            )

            st.divider()

            top_k = st.slider(
                "Retrieved Chunks",
                min_value=1,
                max_value=20,
                value=5,
            )

            summary_type = st.selectbox(
                "Summary Type",
                (
                    "concise",
                    "detailed",
                    "bullet",
                ),
            )

            temperature = st.slider(
                "Temperature",
                min_value=0.0,
                max_value=1.0,
                value=0.2,
                step=0.1,
            )

            st.divider()

            st.caption(
                "Enterprise AI RAG Platform"
            )

        return {
            "task": task,
            "top_k": top_k,
            "summary_type": summary_type,
            "temperature": temperature,
        }