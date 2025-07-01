import streamlit as st
from config.constants import LANGUAGE_OPTIONS
from translations.loader import t
from utils.url_helper import URLHelper

def create_navbar():
    """Create and display the main navigation bar"""
    if 'language' not in st.session_state:
        st.session_state.language = 'pl'

    current_page = URLHelper.get_page_param()
    
    # SIMPLE navbar that ACTUALLY WORKS - no JavaScript bullshit
    st.markdown(f"""
    <style>
    .working-navbar {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 9999;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid #e0e0e0;
        padding: 15px 0;
        box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
    }}
    
    .working-nav-container {{
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px;
    }}
    
    .working-nav-logo {{
        font-size: 28px;
        font-weight: 800;
        background: linear-gradient(135deg, #1a73e8 0%, #34a853 50%, #ea4335 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-decoration: none;
    }}
    
    .working-nav-links {{
        display: flex;
        gap: 30px;
        align-items: center;
    }}
    
    .working-nav-link {{
        color: #5f6368;
        text-decoration: none;
        font-weight: 500;
        font-size: 16px;
        padding: 10px 15px;
        border-radius: 8px;
        transition: all 0.3s ease;
    }}
    
    .working-nav-link:hover {{
        color: #1a73e8;
        background: rgba(26, 115, 232, 0.1);
        transform: translateY(-1px);
    }}
    
    /* Add proper scroll offset for all sections */
    #home, #features, #analytics, #about, #contact {{
        scroll-margin-top: 80px;
    }}
    
    body {{
        padding-top: 80px;
    }}
    
    @media (max-width: 768px) {{
        .working-nav-links {{
            gap: 15px;
        }}
        .working-nav-link {{
            font-size: 14px;
            padding: 8px 10px;
        }}
    }}
    </style>
    
    <div class="working-navbar">
        <div class="working-nav-container">
            <a href="#home" class="working-nav-logo">🔧 aIRONick</a>
            <div class="working-nav-links">
                <a href="#home" class="working-nav-link">{t('navbar.home')}</a>
                <a href="#features" class="working-nav-link">{t('navbar.software_testing')}</a>
                <a href="#analytics" class="working-nav-link">{t('navbar.electrician')}</a>
                <a href="#about" class="working-nav-link">{t('navbar.youtube')}</a>
                <a href="#contact" class="working-nav-link">{t('navbar.contact')}</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Language selector
    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
    with col4:
        st.markdown("""
        <style>
        div[data-testid="column"]:nth-child(4) {
            position: fixed !important;
            top: 20px !important;
            right: 20px !important;
            z-index: 10000 !important;
            width: 100px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
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