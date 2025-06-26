import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json
import os

st.set_page_config(
    page_title="aIRONick",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize language in session state
if 'language' not in st.session_state:
    st.session_state.language = 'pl'

@st.cache_data
def load_translations():
    """Load translation files"""
    translations = {}
    
    # Load Polish translations
    try:
        with open('translations/pl.json', 'r', encoding='utf-8') as f:
            translations['pl'] = json.load(f)
    except FileNotFoundError:
        st.error("Polish translation file not found")
        translations['pl'] = {}
    
    # Load English translations
    try:
        with open('translations/en.json', 'r', encoding='utf-8') as f:
            translations['en'] = json.load(f)
    except FileNotFoundError:
        st.error("English translation file not found")
        translations['en'] = {}
    
    return translations

def get_translation(key, lang=None):
    """Get translation for a key with support for nested keys like 'section.key'"""
    if lang is None:
        lang = st.session_state.language
    
    translations = load_translations()
    
    if lang not in translations:
        return key
    
    # Handle nested keys
    keys = key.split('.')
    value = translations[lang]
    
    try:
        for k in keys:
            value = value[k]
        return value
    except (KeyError, TypeError):
        return key

def t(key):
    """Shorthand for get_translation"""
    return get_translation(key)

def load_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&display=swap');
    
    :root {
        --primary: #1a73e8;
        --primary-hover: #1557b0;
        --secondary: #5f6368;
        --surface: #ffffff;
        --background: #fafafa;
        --text-primary: #202124;
        --text-secondary: #5f6368;
        --border: #dadce0;
        --border-hover: #9aa0a6;
        --matrix-green: #00ff41;
        --shadow: rgba(0, 0, 0, 0.1);
        --shadow-hover: rgba(0, 0, 0, 0.15);
    }
    
    * {
        box-sizing: border-box;
    }
    
    .main > div {
        padding-top: 0rem;
    }
    
    .stApp {
        background: var(--background);
        color: var(--text-primary);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    .stApp > header {
        background-color: transparent;
    }
    
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid var(--border);
        padding: 1rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 1px 6px var(--shadow);
    }
    
    .navbar-brand {
        font-family: 'Orbitron', monospace;
        font-size: 1.5rem;
        font-weight: 900;
        color: var(--matrix-green);
        text-decoration: none;
        text-shadow: 0 0 8px rgba(0, 255, 65, 0.3);
        letter-spacing: 1px;
        animation: matrix-glow 3s ease-in-out infinite;
    }
    
    @keyframes matrix-glow {
        0%, 100% { text-shadow: 0 0 8px rgba(0, 255, 65, 0.3); }
        50% { text-shadow: 0 0 16px rgba(0, 255, 65, 0.6), 0 0 24px rgba(0, 255, 65, 0.4); }
    }
    
    .navbar-nav {
        display: flex;
        list-style: none;
        margin: 0;
        padding: 0;
        gap: 0;
    }
    
    .nav-link {
        color: var(--text-secondary);
        text-decoration: none;
        font-weight: 400;
        transition: all 0.2s ease;
        padding: 0.75rem 1.25rem;
        border-radius: 8px;
        font-size: 0.9rem;
    }
    
    .nav-link:hover {
        color: var(--primary);
        background: rgba(26, 115, 232, 0.08);
    }
    
    .hero-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        color: var(--text-primary);
        padding: 8rem 2rem 5rem 2rem;
        text-align: center;
        margin-top: 0;
    }
    
    .hero-title {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        color: var(--text-primary);
        line-height: 1.1;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        margin-bottom: 2rem;
        color: var(--text-secondary);
        font-weight: 400;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.5;
    }
    
    .section {
        padding: 5rem 2rem;
        margin: 0;
        background: var(--surface);
    }
    
    .section:nth-child(even) {
        background: var(--background);
    }
    
    .section-title {
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 3rem;
        color: var(--text-primary);
        font-weight: 600;
        line-height: 1.2;
    }
    
    .card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 2px 8px var(--shadow);
        margin-bottom: 1.5rem;
        transition: all 0.2s ease;
    }
    
    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px var(--shadow-hover);
        border-color: var(--border-hover);
    }
    
    .card h3 {
        color: var(--text-primary);
        font-weight: 600;
        font-size: 1.25rem;
        margin-bottom: 1rem;
        line-height: 1.3;
    }
    
    .card p {
        color: var(--text-secondary);
        line-height: 1.6;
        font-size: 0.95rem;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .metric-card {
        background: var(--surface);
        color: var(--text-primary);
        padding: 2rem;
        border: 1px solid var(--border);
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 2px 8px var(--shadow);
        transition: all 0.2s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px var(--shadow-hover);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: var(--primary);
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: var(--text-secondary);
        font-weight: 500;
    }
    
    .footer {
        background: var(--surface);
        color: var(--text-secondary);
        padding: 3rem 2rem;
        text-align: center;
        border-top: 1px solid var(--border);
        font-size: 0.9rem;
    }
    
    .stButton > button {
        background: var(--primary);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.2s ease;
        font-size: 0.9rem;
    }
    
    .stButton > button:hover {
        background: var(--primary-hover);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(26, 115, 232, 0.3);
    }
    
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: var(--surface);
        color: var(--text-primary);
        border: 1px solid var(--border);
        border-radius: 8px;
        font-family: inherit;
        transition: border-color 0.2s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--primary);
        box-shadow: 0 0 0 3px rgba(26, 115, 232, 0.1);
    }
    
    .cta-button {
        display: inline-block;
        background: var(--primary);
        color: white;
        padding: 1rem 2rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.2s ease;
        margin-top: 1rem;
    }
    
    .cta-button:hover {
        background: var(--primary-hover);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(26, 115, 232, 0.3);
    }
    
    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            padding: 1rem;
        }
        
        .navbar-nav {
            margin-top: 1rem;
            flex-wrap: wrap;
            justify-content: center;
            gap: 0.25rem;
        }
        
        .hero-title {
            font-size: 2.5rem;
        }
        
        .hero-section {
            padding: 6rem 1rem 4rem 1rem;
        }
        
        .section {
            padding: 3rem 1rem;
        }
        
        .feature-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def create_navbar():
    if 'language' not in st.session_state:
        st.session_state.language = 'pl'

    # Sticky navbar CSS and JavaScript
    st.markdown("""
    <style>
    .sticky-navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid #dadce0;
        padding: 15px 30px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    .navbar-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
    }
    .menu-items {
        display: flex;
        align-items: center;
        gap: 30px;
    }
    .menu-link {
        text-decoration: none;
        color: #5f6368;
        font-weight: 400;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        padding: 8px 16px;
        border-radius: 8px;
    }
    .menu-link:hover {
        color: #1f77b4;
        background: rgba(31, 119, 180, 0.1);
    }
    .menu-link.active {
        color: #1f77b4;
        background: rgba(31, 119, 180, 0.15);
        border-bottom: 2px solid #1f77b4;
    }
    .logo {
        font-weight: bold;
        font-size: 2rem;
        color: #00ff41;
    }
    body {
        padding-top: 80px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Jedna linia z logo, menu i dropdownem
    col1, col2 = st.columns([5, 1])

    with col1:
        st.markdown("""
        <div class="sticky-navbar">
            <div class="navbar-content">
                <div class="menu-items">
                    <div class="logo">🤖 aIRONick</div>
                    <a href="#home" class="menu-link" id="menu-home" onclick="scrollToSection('home')">Start</a>
                    <a href="#features" class="menu-link" id="menu-features" onclick="scrollToSection('features')">Testowanie oprogramowania</a>
                    <a href="#analytics" class="menu-link" id="menu-analytics" onclick="scrollToSection('analytics')">Elektryk</a>
                    <a href="#about" class="menu-link" id="menu-about" onclick="scrollToSection('about')">YouTube</a>
                    <a href="#contact" class="menu-link" id="menu-contact" onclick="scrollToSection('contact')">Kontakt</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Add JavaScript separately
        st.markdown("""
        <script>
        function scrollToSection(sectionId) {
            const element = document.getElementById(sectionId);
            if (element) {
                element.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
        
        // Highlight active menu item based on scroll position
        function updateActiveMenu() {
            const sections = ['home', 'features', 'analytics', 'about', 'contact'];
            
            sections.forEach(section => {
                const element = document.getElementById(section);
                const menuLink = document.getElementById('menu-' + section);
                
                if (element && menuLink) {
                    const rect = element.getBoundingClientRect();
                    const isInView = rect.top <= 100 && rect.bottom >= 100;
                    
                    if (isInView) {
                        // Remove active class from all menu items
                        document.querySelectorAll('.menu-link').forEach(link => {
                            link.classList.remove('active');
                        });
                        // Add active class to current menu item
                        menuLink.classList.add('active');
                    }
                }
            });
        }
        
        // Update active menu on scroll
        window.addEventListener('scroll', updateActiveMenu);
        // Update active menu on load
        window.addEventListener('load', updateActiveMenu);
        </script>
        """, unsafe_allow_html=True)

    # Language dropdown integrated into sticky navbar
    st.markdown(f"""
    <div style="position: fixed; top: 25px; right: 30px; z-index: 1000;">
        <select onchange="changeLanguage(this.value)" style="
            padding: 8px 12px;
            border: 1px solid #dadce0;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.95);
            font-size: 1rem;
            color: #5f6368;
            cursor: pointer;
            backdrop-filter: blur(10px);
        ">
            <option value="pl" {'selected' if st.session_state.language == 'pl' else ''}>🇵🇱 PL</option>
            <option value="en" {'selected' if st.session_state.language == 'en' else ''}>🇬🇧 EN</option>
        </select>
    </div>
    <script>
    function changeLanguage(lang) {{
        // This would need to trigger a Streamlit rerun
        // For now, we'll use the existing selectbox approach
        console.log('Language changed to:', lang);
    }}
    </script>
    """, unsafe_allow_html=True)
    
    # Keep the original selectbox hidden but functional
    with col2:
        language_options = {"🇵🇱 PL": "pl", "🇬🇧 EN": "en"}
        
        # Hide the selectbox visually but keep it functional
        st.markdown("""
        <style>
        div[data-testid="stSelectbox"] {
            display: none !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        selected = st.selectbox(
            "",
            list(language_options.keys()),
            key="language_selector",
            label_visibility="collapsed"
        )

        new_lang = language_options[selected]
        if new_lang != st.session_state.language:
            st.session_state.language = new_lang
            st.rerun()

def create_hero_section():
    st.markdown(f"""
    <div class="hero-section" id="home" style="padding-top: 120px;">
        <h1 class="hero-title">{t('hero.title')}</h1>
        <p class="hero-subtitle">{t('hero.subtitle')}</p>
    </div>
    """, unsafe_allow_html=True)

def create_features_section():
    st.markdown(f"""
    <div class="section" id="features">
        <h2 class="section-title">{t('features.title')}</h2>
        <div class="feature-grid">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="card">
            <h3>🔧 {t('features.software_testing.title')}</h3>
            <p>{t('features.software_testing.description')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="card">
            <h3>🎮 {t('features.gaming_solutions.title')}</h3>
            <p>{t('features.gaming_solutions.description')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="card">
            <h3>⚡ {t('features.hardware_testing.title')}</h3>
            <p>{t('features.hardware_testing.description')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="card">
            <h3>🔌 {t('features.electrical_services.title')}</h3>
            <p>{t('features.electrical_services.description')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

def create_analytics_section():
    st.markdown(f"""
    <div class="section" id="analytics">
        <h2 class="section-title">{t('electrician.title')}</h2>
        <div class="feature-grid">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="card">
            <h3>⚡ {t('electrician.residential.title')}</h3>
            <p>{t('electrician.residential.description')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="card">
            <h3>🏢 {t('electrician.commercial.title')}</h3>
            <p>{t('electrician.commercial.description')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="card">
            <h3>🔧 {t('electrician.troubleshooting.title')}</h3>
            <p>{t('electrician.troubleshooting.description')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="card">
            <h3>🔌 {t('electrician.smart_home.title')}</h3>
            <p>{t('electrician.smart_home.description')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

def create_about_section():
    st.markdown(f"""
    <div class="section" id="about">
        <h2 class="section-title">{t('youtube.title')}</h2>
    """, unsafe_allow_html=True)
    
    st.markdown(f"### 🎥 {t('youtube.watch_videos')}")
    st.write(t('youtube.description'))
    
    # Create centered button using Streamlit
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(f"🚀 {t('youtube.visit_channel')}", key="youtube_btn"):
            st.markdown('<meta http-equiv="refresh" content="0; url=https://www.youtube.com/@aIrOnick">', unsafe_allow_html=True)
        st.markdown("""
        <style>
        .stButton > button {
            background: linear-gradient(45deg, #ff0000, #cc0000);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 25px;
            font-weight: bold;
            font-size: 16px;
            width: 100%;
        }
        .stButton > button:hover {
            transform: scale(1.05);
            transition: transform 0.3s ease;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Featured playlists section
    st.markdown(f"### 📺 {t('youtube.featured_playlists')}")
    
    # Create playlist cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="card" style="text-align: center;">
            <h4>🔧 {t('youtube.playlist_software_testing')}</h4>
            <p>{t('youtube.playlist_software_testing_desc')}</p>
            <a href="https://www.youtube.com/@aIrOnick/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ {t('youtube.watch_playlist')}</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="card" style="text-align: center;">
            <h4>🎮 {t('youtube.playlist_gaming_tech')}</h4>
            <p>{t('youtube.playlist_gaming_tech_desc')}</p>
            <a href="https://www.youtube.com/@aIrOnick/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ {t('youtube.watch_playlist')}</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="card" style="text-align: center;">
            <h4>⚡ {t('youtube.playlist_electrical_work')}</h4>
            <p>{t('youtube.playlist_electrical_work_desc')}</p>
            <a href="https://www.youtube.com/@aIrOnick/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ {t('youtube.watch_playlist')}</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="card" style="text-align: center;">
            <h4>💻 {t('youtube.playlist_hardware_reviews')}</h4>
            <p>{t('youtube.playlist_hardware_reviews_desc')}</p>
            <a href="https://www.youtube.com/@aIrOnick/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ {t('youtube.watch_playlist')}</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def create_contact_section():
    st.markdown(f"""
    <div class="section" id="contact">
        <h2 class="section-title">{t('contact.title')}</h2>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="card">
            <h3>{t('contact.get_in_touch')}</h3>
            <p>📧 {t('contact.email')}: kontakt@aironick.com</p>
            <p>📱 {t('contact.phone')}: +48 730 379 623</p>
            <p>🌐 {t('contact.website')}: www.aironick.com</p>
            <p>📍 {t('contact.service_area')}: {t('contact.service_area_value')}</p>
            <p>⏰ {t('contact.hours')}: {t('contact.hours_value')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader(t('contact.send_message'))
        
        with st.form("contact_form"):
            name = st.text_input(t('contact.your_name'))
            email = st.text_input(t('contact.email_address'))
            service = st.selectbox(t('contact.service_needed'), [t('contact.software_testing'), t('contact.hardware_testing'), t('contact.electrical_services'), t('contact.gaming_solutions'), t('contact.multiple_services'), t('contact.consultation')])
            message = st.text_area(t('contact.project_details'), height=100, placeholder=t('contact.project_placeholder'))
            
            if st.form_submit_button(t('contact.request_quote')):
                if name and email and message:
                    st.success(t('contact.success_message'))
                else:
                    st.error(t('contact.error_message'))
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def create_footer():
    st.markdown(f"""
    <div class="footer">
        <p>{t('footer.copyright')}</p>
        <p>{t('footer.services')}</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    load_custom_css()
    create_navbar()
    create_hero_section()
    create_features_section()
    create_analytics_section()
    create_about_section()
    create_contact_section()
    create_footer()

if __name__ == "__main__":
    main()