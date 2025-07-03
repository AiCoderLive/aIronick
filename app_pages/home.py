import streamlit as st
from components.navbar import create_navbar, create_main_tabs
from components.hero import create_hero_section
from components.features import create_features_section
from components.analytics import create_analytics_section
from components.about import create_about_section
from components.contact import create_contact_section
from components.footer import create_footer

def show_home_page():
    """Display the main home page using tabs navigation"""
    
    create_navbar()
    
    # Create tabs for navigation
    tab1, tab2, tab3, tab4, tab5 = create_main_tabs()
    
    with tab1:
        create_hero_section()
    
    with tab2:
        create_features_section()
    
    with tab3:
        create_analytics_section()
    
    with tab4:
        create_about_section()
    
    with tab5:
        create_contact_section()
    
    create_footer()