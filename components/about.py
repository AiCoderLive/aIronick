import streamlit as st
from translations.loader import t
from config.constants import CONTACT_INFO

def create_about_section():
    """Create and display the about/YouTube section"""
    st.markdown(f"""
    <div class="section" id="about" style="padding-top: 100px;">
        <h2 class="section-title">{t('youtube.title')}</h2>
    """, unsafe_allow_html=True)

    st.markdown(f"### 🎥 {t('youtube.watch_videos')}")
    st.write(t('youtube.description'))

    # Create centered button using Streamlit
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(f"🚀 {t('youtube.visit_channel')}", key="youtube_btn"):
            st.markdown(f'<meta http-equiv="refresh" content="0; url={CONTACT_INFO["youtube"]}">',
                        unsafe_allow_html=True)
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
            <a href="{CONTACT_INFO["youtube"]}/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ {t('youtube.watch_playlist')}</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="card" style="text-align: center;">
            <h4>🎮 {t('youtube.playlist_gaming_tech')}</h4>
            <p>{t('youtube.playlist_gaming_tech_desc')}</p>
            <a href="{CONTACT_INFO["youtube"]}/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ {t('youtube.watch_playlist')}</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card" style="text-align: center;">
            <h4>⚡ {t('youtube.playlist_electrical_work')}</h4>
            <p>{t('youtube.playlist_electrical_work_desc')}</p>
            <a href="{CONTACT_INFO["youtube"]}/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ {t('youtube.watch_playlist')}</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="card" style="text-align: center;">
            <h4>💻 {t('youtube.playlist_hardware_reviews')}</h4>
            <p>{t('youtube.playlist_hardware_reviews_desc')}</p>
            <a href="{CONTACT_INFO["youtube"]}/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ {t('youtube.watch_playlist')}</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)