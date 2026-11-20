"""
Insight Panel
"""

import streamlit as st

from ui.components import UIComponents


class InsightPanel:

    @staticmethod
    def render(
        insight_service,
        settings,
    ):

        st.subheader(
            "💡 Document Insights"
        )

        if not UIComponents.require_documents():
            return

        
        if st.button(
            "Generate Insights",
            use_container_width=True,
        ):

            with UIComponents.loading(
                "Generating insights..."
            ):

                insights = insight_service.generate(
                    top_k=settings["top_k"],
                ) 
                st.session_state.insights = insights

        if st.session_state.insights:

            st.markdown(
                st.session_state.insights
            )