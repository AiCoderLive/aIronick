import streamlit as st
from styles.base import load_base_css
from styles.components import load_components_css
from components.navbar import create_navbar
from components.hero import create_hero_section
from components.features import create_features_section
from components.analytics import create_analytics_section
from components.about import create_about_section
from components.contact import create_contact_section
from components.footer import create_footer

def show_home_page():
    """Display the main home page"""
    
    # Ensure clean interface without any sidebar elements
    st.markdown("""
    <style>
    /* Hide any potential sidebar elements */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Ensure full width for main content */
    .main .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: none !important;
        margin-left: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    load_base_css()
    load_components_css()
    
    create_navbar()
    create_hero_section()
    create_features_section()
    create_analytics_section()
    create_about_section()
    create_contact_section()
    create_footer()