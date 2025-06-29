import streamlit as st
from translations.loader import t

def create_footer():
    """Create and display the footer section"""
    st.markdown(f"""
    <div class="footer">
        <p>{t('footer.copyright')}</p>
        <p>{t('footer.services')}</p>
    </div>
    """, unsafe_allow_html=True)