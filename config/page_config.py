import streamlit as st

def setup_page_config(sidebar_state="collapsed"):
    """Configure Streamlit page settings"""
    st.set_page_config(
        page_title="aIRONick",
        page_icon="💻",
        layout="wide",
        initial_sidebar_state=sidebar_state
    )

def initialize_language():
    """Initialize language in session state"""
    if 'language' not in st.session_state:
        st.session_state.language = 'pl'