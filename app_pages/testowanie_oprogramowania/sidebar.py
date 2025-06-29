import streamlit as st
from config.constants import LANGUAGE_OPTIONS

def create_testing_sidebar():
    """Create sidebar for testing page"""
    with st.sidebar:
        st.markdown("### 🔧 Testowanie Oprogramowania")
        
        # Navigation menu
        if 'selected_section' not in st.session_state:
            st.session_state.selected_section = 'overview'
        
        menu_items = {
            'overview': '📋 Informacje ogolne' if st.session_state.language == 'pl' else '📋 Overview',
            'automatic': '🤖 Testowanie automatyczne' if st.session_state.language == 'pl' else '🤖 Automatic Testing',
            'performance': '⚡ Testowanie wydajnościowe' if st.session_state.language == 'pl' else '⚡ Performance Testing'
        }
        
        for key, label in menu_items.items():
            if st.button(label, key=f"testing_menu_{key}", use_container_width=True):
                st.session_state.selected_section = key