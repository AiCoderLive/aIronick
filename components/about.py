import streamlit as st
from translations.loader import t
from config.constants import CONTACT_INFO

def create_about_section():
    """Create and display the about/YouTube section using pure Streamlit"""
        
    # About section
    st.markdown("---")
    st.markdown("## " + t('youtube.title'))

    st.markdown("### 🎥 " + t('youtube.watch_videos'))
    st.write(t('youtube.description'))

    # Create centered button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(f"🚀 {t('youtube.visit_channel')}", key="youtube_btn", use_container_width=True):
            st.link_button("Otwórz YouTube", CONTACT_INFO["youtube"])

    st.markdown("<br>", unsafe_allow_html=True)

    # Featured playlists section
    st.markdown("### 📺 " + t('youtube.featured_playlists'))

    # Create playlist cards
    col1, col2 = st.columns(2)

    with col1:
        with st.container():
            st.markdown("#### 🔧 " + t('youtube.playlist_software_testing'))
            st.markdown(t('youtube.playlist_software_testing_desc'))
            st.link_button("▶️ " + t('youtube.watch_playlist'), f"{CONTACT_INFO['youtube']}/playlists", use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown("#### 🎮 " + t('youtube.playlist_gaming_tech'))
            st.markdown(t('youtube.playlist_gaming_tech_desc'))
            st.link_button("▶️ " + t('youtube.watch_playlist'), f"{CONTACT_INFO['youtube']}/playlists", use_container_width=True)

    with col2:
        with st.container():
            st.markdown("#### ⚡ " + t('youtube.playlist_electrical_work'))
            st.markdown(t('youtube.playlist_electrical_work_desc'))
            st.link_button("▶️ " + t('youtube.watch_playlist'), f"{CONTACT_INFO['youtube']}/playlists", use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown("#### 💻 " + t('youtube.playlist_hardware_reviews'))
            st.markdown(t('youtube.playlist_hardware_reviews_desc'))
            st.link_button("▶️ " + t('youtube.watch_playlist'), f"{CONTACT_INFO['youtube']}/playlists", use_container_width=True)