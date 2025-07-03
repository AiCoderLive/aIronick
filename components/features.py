import streamlit as st
from translations.loader import t
from utils.url_helper import URLHelper

def create_features_section():
    """Create and display the features section using pure Streamlit"""
        
    # Features section header
    st.markdown("---")
    st.markdown("## " + t('features.title'))
    
    # Single comprehensive software testing section
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown("### 🔧 " + t('features.software_testing.title'))
        st.markdown(t('features.software_testing.description'))
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Navigation button
        if st.button("📋 Zobacz więcej", key="zobacz_wiecej_btn", help="Przejdź do strony testowania oprogramowania", use_container_width=True):
            URLHelper.navigate_to_page("testowanie_oprogramowania")