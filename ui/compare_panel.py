"""
Compare Panel
"""

import streamlit as st

from ui.components import UIComponents


class ComparePanel:

    @staticmethod
    def render(
        compare_service,
    ):

        st.subheader(
            "📄 Compare Documents"
        )

        context_a = st.text_area(
            "Document A"
        )

        context_b = st.text_area(
            "Document B"
        )

        if st.button(
            "Compare",
            use_container_width=True,
        ):

            if not context_a.strip() or not context_b.strip():

                UIComponents.warning(
                    "Both document contexts are required."
                )

                return

            with UIComponents.loading(
                "Comparing..."
            ):

                result = compare_service.compare(
                    context_a=context_a,
                    context_b=context_b,
                )

                st.markdown(
                    result
                )