"""
DocMind-AI

Application Entry Point
"""

import streamlit as st

from core.container import ApplicationContainer

from ui.session_state import SessionState
from ui.sidebar import Sidebar
from ui.dashboard import Dashboard
from ui.uploader import Uploader
from ui.chat import ChatUI
from ui.summary_panel import SummaryPanel
from ui.keyword_panel import KeywordPanel
from ui.insight_panel import InsightPanel
from ui.compare_panel import ComparePanel


def main():
    """
    Launch the Streamlit application.
    """

    st.set_page_config(
        page_title="DocMind-AI",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # ---------------------------------------------------------
    # Initialize Session
    # ---------------------------------------------------------

    SessionState.initialize()

    # ---------------------------------------------------------
    # Dependency Injection
    # ---------------------------------------------------------
    if st.session_state.container is None:
        st.session_state.container = ApplicationContainer()

    container = st.session_state.container
    

    # ---------------------------------------------------------
    # Sidebar
    # ---------------------------------------------------------

    settings = Sidebar.render()

    st.session_state.settings = settings

    # ---------------------------------------------------------
    # Dashboard
    # ---------------------------------------------------------

    Dashboard.render()

    # ---------------------------------------------------------
    # Document Upload
    # ---------------------------------------------------------
    Uploader.render(container)

# ---------------------------------------------------------
# AI Task Selection
# ---------------------------------------------------------

    task = settings["task"]

    if task == "Question Answering":

        ChatUI.render(
        qa_service=container.qa_service,
        settings=settings,
    )
    
    elif task == "Summary":

        SummaryPanel.render(
            summary_service=container.summary_service,
            settings=settings,
        )

    elif task == "Keyword Extraction":

        KeywordPanel.render(
            keyword_service=container.keyword_service,
            settings=settings,
        )

    elif task == "Insights":

        InsightPanel.render(
            insight_service=container.insight_service,
            settings=settings,
        )

    elif task == "Compare Documents":

        ComparePanel.render(
            compare_service=container.compare_service,
        )


if __name__ == "__main__":
    main()