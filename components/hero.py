import streamlit as st
from translations.loader import t

def create_hero_section():
    """Create and display the hero section"""
    st.markdown(f"""
    <div class="hero-section" id="home" style="padding-top: 120px;">
        <h1 class="hero-title">{t('hero.title')}</h1>
        <p class="hero-subtitle">{t('hero.subtitle')}</p>
    </div>
    """, unsafe_allow_html=True)