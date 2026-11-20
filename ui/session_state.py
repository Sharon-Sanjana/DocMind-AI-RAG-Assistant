"""
Session State

Initializes and manages
Streamlit session state.
"""

import streamlit as st


class SessionState:
    """
    Manages Streamlit session variables.
    """

    @staticmethod
    def initialize():
        """
        Initialize session variables.
        """

        defaults = {

            "messages": [],

            "uploaded_documents": [],

            "selected_document": None,

            "summary": None,

            "comparison": None,

            "keywords": None,

            "insights": None,
            "container": None,

            "settings": {},
        }

        for key, value in defaults.items():

            if key not in st.session_state:

                st.session_state[key] = value