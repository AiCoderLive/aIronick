import streamlit as st
from config.constants import LANGUAGE_OPTIONS
from translations.loader import t
from styles.navbar import load_navbar_css
from utils.url_helper import URLHelper

def create_navbar():
    """Create and display the main navigation bar"""
    if 'language' not in st.session_state:
        st.session_state.language = 'pl'

    load_navbar_css()
    current_page = URLHelper.get_page_param()
    home_url = URLHelper.get_home_url()
    
    # Simple navigation - if on testing page, go home; if on home, use anchors
    if current_page == "testowanie_oprogramowania":
        home_link = home_url
        features_link = home_url  
        analytics_link = home_url
        about_link = home_url
        contact_link = home_url
    else:
        home_link = "#home"
        features_link = "#features"
        analytics_link = "#analytics"
        about_link = "#about" 
        contact_link = "#contact"
    
    st.markdown(f"""
    <div class="sticky-navbar">
        <div class="navbar-content">
            <div class="menu-items">
                <div class="logo"><span class="chip-icon"></span> aIRONick</div>
                <a href="{home_link}" class="menu-link">{t('navbar.home')}</a>
                <a href="{features_link}" class="menu-link">{t('navbar.software_testing')}</a>
                <a href="{analytics_link}" class="menu-link">{t('navbar.electrician')}</a>
                <a href="{about_link}" class="menu-link">{t('navbar.youtube')}</a>
                <a href="{contact_link}" class="menu-link">{t('navbar.contact')}</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Language dropdown  
    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
    with col4:
        selected = st.selectbox(
            "",
            list(LANGUAGE_OPTIONS.keys()),
            index=0 if st.session_state.language == 'pl' else 1,
            key="language_selector",
            label_visibility="collapsed"
        )

        new_lang = LANGUAGE_OPTIONS[selected]
        if new_lang != st.session_state.language:
            st.session_state.language = new_lang
            st.rerun()