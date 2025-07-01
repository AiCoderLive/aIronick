import streamlit as st
from translations.loader import t

def create_analytics_section():
    """Create and display the analytics/electrician section"""
    st.markdown(f"""
    <div class="section" id="analytics" style="padding-top: 100px;">
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