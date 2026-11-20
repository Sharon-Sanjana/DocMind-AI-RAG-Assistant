"""
Reusable UI Components
"""

from contextlib import contextmanager

import streamlit as st


class UIComponents:
    """
    Reusable Streamlit components.
    """

    @staticmethod
    def require_documents() -> bool:
        """
        Ensure at least one document
        has been uploaded.
        """

        if not st.session_state.uploaded_documents:
            st.warning(
                "Please upload at least one document first."
            )
            return False

        return True

    @staticmethod
    def page_title(
        title: str,
        subtitle: str = "",
    ):
        """
        Render page title.
        """

        st.title(title)

        if subtitle:
            st.caption(subtitle)

        st.divider()

    @staticmethod
    def success(
        message: str,
    ):
        """
        Success message.
        """

        st.success(message)

    @staticmethod
    def error(
        message: str,
    ):
        """
        Error message.
        """

        st.error(message)

    @staticmethod
    def warning(
        message: str,
    ):
        """
        Warning message.
        """

        st.warning(message)

    @staticmethod
    def info(
        message: str,
    ):
        """
        Information message.
        """

        st.info(message)

    @staticmethod
    def metric_card(
        title: str,
        value,
    ):
        """
        Metric card.
        """

        st.metric(
            title,
            value,
        )

    @staticmethod
    @contextmanager
    def loading(
        message: str = "Processing...",
    ):
        """
        Loading spinner.
        """

        with st.spinner(message):
            yield