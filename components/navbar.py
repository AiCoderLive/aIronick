import streamlit as st
from config.constants import LANGUAGE_OPTIONS
from translations.loader import t


def create_navbar():
    """Create simple Streamlit navigation header with language selector"""
    if 'language' not in st.session_state:
        st.session_state.language = 'pl'

    # Simple header with logo and language selector
    logo_col, lang_col = st.columns([4, 1])
    
    with logo_col:
        st.markdown("# 💻 aIRONick")
    
    with lang_col:
        # Language selector
        selected = st.selectbox(
            "Język",
            list(LANGUAGE_OPTIONS.keys()),
            index=0 if st.session_state.language == 'pl' else 1,
            key="language_selector",
            label_visibility="collapsed"
        )

        new_lang = LANGUAGE_OPTIONS[selected]
        if new_lang != st.session_state.language:
            st.session_state.language = new_lang
            st.rerun()

def create_main_tabs():
    """Create main navigation tabs"""
    # Tab labels
    tab_labels = [
        t('navbar.home'),
        t('navbar.software_testing'), 
        t('navbar.electrician'),
        t('navbar.youtube'),
        t('navbar.contact')
    ]
    
    return st.tabs(tab_labels)