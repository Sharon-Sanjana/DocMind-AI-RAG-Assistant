"""
Summary Panel

Displays document summarization UI.
"""

import streamlit as st

from ui.components import UIComponents


class SummaryPanel:
    """
    Summary interface.
    """

    @staticmethod
    def render(
        summary_service,
        settings,
    ):
        """
        Render summary panel.
        """

        st.subheader("📝 Document Summary")

        summary_type = st.selectbox(
            "Summary Type",
            (
                "concise",
                "detailed",
                "bullet",
            ),
            key="summary_type_panel",
        )

        if not UIComponents.require_documents():
            return
        
        if st.button(
            "Generate Summary",
            use_container_width=True,
        ):

            with UIComponents.loading(
                "Generating summary..."
            ):

                summary = summary_service.summarize(
                    summary_type=summary_type,
                    top_k=settings["top_k"],

                )

                st.session_state.summary = summary

        if st.session_state.summary:

            st.markdown(
                st.session_state.summary
            )