import streamlit as st
from components.navbar import create_navbar
from .sidebar import create_testing_sidebar
from .sections.overview import create_overview_section
from .sections.automatic import create_automatic_testing_section
from .sections.performance import create_performance_testing_section
from utils.url_helper import URLHelper

def show_testing_page():
    """Display the software testing page using pure Streamlit"""
    
    # Initialize session state for selected section
    if 'selected_section' not in st.session_state:
        st.session_state.selected_section = 'overview'
    
    # Add top navigation menu
    create_navbar()
    
    create_testing_sidebar()
    
    # Page header
    st.markdown("# 🔧 Testowanie Oprogramowania")
    st.markdown("#### Profesjonalne usługi testowania oprogramowania - automatyzacja, wydajność, jakość")
    st.markdown("---")
    
    # Main content based on selected section
    if st.session_state.selected_section == 'overview':
        create_overview_section()
    elif st.session_state.selected_section == 'automatic':
        create_automatic_testing_section()
    elif st.session_state.selected_section == 'performance':
        create_performance_testing_section()