import streamlit as st
from translations.loader import t

def create_features_section():
    """Create and display the features section"""
    st.markdown(f"""
    <div class="section" id="features">
        <h2 class="section-title">{t('features.title')}</h2>
        <div class="feature-grid">
    """, unsafe_allow_html=True)

    # Single comprehensive software testing section
    st.markdown(f"""
    <div class="card" style="max-width: 800px; margin: 0 auto; padding: 3rem;">
        <h3 style="font-size: 1.8rem; margin-bottom: 1.5rem;">🔧 {t('features.software_testing.title')}</h3>
        <p style="font-size: 1.1rem; line-height: 1.7; margin-bottom: 2rem;">{t('features.software_testing.description')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create button using Streamlit's native button component
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Add custom CSS for the button
        st.markdown("""
        <style>
        .stButton > button {
            width: 100%;
            background: #1a73e8;
            color: white;
            padding: 1rem 2rem;
            border-radius: 8px;
            border: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(26, 115, 232, 0.3);
        }
        .stButton > button:hover {
            background: #1557b0;
            transform: translateY(-1px);
            box-shadow: 0 6px 16px rgba(26, 115, 232, 0.4);
        }
        </style>
        """, unsafe_allow_html=True)
        
        if st.button("📋 Zobacz więcej", key="zobacz_wiecej_btn", help="Przejdź do strony testowania oprogramowania"):
            try:
                st.query_params["page"] = "testowanie_oprogramowania"
            except AttributeError:
                # Fallback for older Streamlit versions
                st.experimental_set_query_params(page="testowanie_oprogramowania")
            st.rerun()

    st.markdown("</div></div>", unsafe_allow_html=True)