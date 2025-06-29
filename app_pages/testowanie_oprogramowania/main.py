import streamlit as st
from styles.base import load_base_css
from styles.testing_page import load_testing_page_css
from components.navbar import create_navbar
from .sidebar import create_testing_sidebar
from .sections.overview import create_overview_section
from .sections.automatic import create_automatic_testing_section
from .sections.performance import create_performance_testing_section

def show_testing_page():
    """Display the software testing page"""
    load_base_css()
    load_testing_page_css()
    
    # Add top navigation menu
    create_navbar()
    
    create_testing_sidebar()
    
    # Main content wrapper with top padding
    st.markdown('<div style="padding-top: 100px;">', unsafe_allow_html=True)
    
    # Back button
    st.markdown('<a href="?" class="back-button">← Powrót do strony głównej</a>', unsafe_allow_html=True)
    
    # Page header
    st.markdown("""
    <div class="page-header">
        <h1 class="page-title">🔧 Testowanie Oprogramowania</h1>
        <p class="page-subtitle">Profesjonalne usługi testowania oprogramowania - automatyzacja, wydajność, jakość</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Main content based on selected section
    if st.session_state.selected_section == 'overview':
        create_overview_section()
    elif st.session_state.selected_section == 'automatic':
        create_automatic_testing_section()
    elif st.session_state.selected_section == 'performance':
        create_performance_testing_section()