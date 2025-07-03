import streamlit as st
from translations.loader import t

def create_analytics_section():
    """Create and display the analytics/electrician section using pure Streamlit"""
        
    # Analytics section
    st.markdown("---")
    st.markdown("## " + t('electrician.title'))

    col1, col2 = st.columns(2)

    with col1:
        with st.container():
            st.markdown("### ⚡ " + t('electrician.residential.title'))
            st.markdown(t('electrician.residential.description'))
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown("### 🏢 " + t('electrician.commercial.title'))
            st.markdown(t('electrician.commercial.description'))

    with col2:
        with st.container():
            st.markdown("### 🔧 " + t('electrician.troubleshooting.title'))
            st.markdown(t('electrician.troubleshooting.description'))
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown("### 🔌 " + t('electrician.smart_home.title'))
            st.markdown(t('electrician.smart_home.description'))