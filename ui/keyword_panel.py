"""
Keyword Panel
"""

import streamlit as st

from ui.components import UIComponents


class KeywordPanel:

    @staticmethod
    def render(
        keyword_service,
        settings,
    ):

        st.subheader(
            "🔑 Keyword Extraction"
        )

        if not UIComponents.require_documents():
            return

        if st.button(
            "Extract Keywords",
            use_container_width=True,
        ):

            with UIComponents.loading(
                "Extracting..."
            ):
                keywords = keyword_service.extract(
                    top_k=settings["top_k"],
                )
                

                st.session_state.keywords = keywords

        if st.session_state.keywords:

            st.markdown(
                st.session_state.keywords
            )