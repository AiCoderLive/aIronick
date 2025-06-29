import streamlit as st
from config.constants import LANGUAGE_OPTIONS

def create_testing_sidebar():
    """Create sidebar for testing page"""
    with st.sidebar:
        st.markdown("### 🔧 Testowanie Oprogramowania")
        
        # Language selector
        current_display = "🇵🇱 Polski" if st.session_state.language == 'pl' else "🇬🇧 English"
        selected = st.selectbox(
            "Język / Language",
            list(LANGUAGE_OPTIONS.keys()),
            index=0 if st.session_state.language == 'pl' else 1,
            key="testing_language_selector"
        )
        
        new_lang = LANGUAGE_OPTIONS[selected]
        if new_lang != st.session_state.language:
            st.session_state.language = new_lang
            st.rerun()
        
        st.markdown("---")
        
        # Navigation menu
        if 'selected_section' not in st.session_state:
            st.session_state.selected_section = 'overview'
        
        menu_items = {
            'overview': '📋 Przegląd' if st.session_state.language == 'pl' else '📋 Overview',
            'automatic': '🤖 Testowanie automatyczne' if st.session_state.language == 'pl' else '🤖 Automatic Testing',
            'performance': '⚡ Testowanie wydajnościowe' if st.session_state.language == 'pl' else '⚡ Performance Testing'
        }
        
        for key, label in menu_items.items():
            if st.button(label, key=f"testing_menu_{key}", use_container_width=True):
                st.session_state.selected_section = key
                st.rerun()