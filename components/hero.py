import streamlit as st
from translations.loader import t

def create_hero_section():
    """Create and display the hero section using pure Streamlit"""
    
    # Hero section with pure Streamlit
    st.container()
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("# " + t('hero.title'))
        st.markdown("#### " + t('hero.subtitle'))
        
        # Add some spacing
        st.markdown("<br>", unsafe_allow_html=True)