import streamlit as st
from config.constants import LANGUAGE_OPTIONS
from translations.loader import t
from styles.navbar import load_navbar_css


def create_navbar():
    """Create and display the main navigation bar"""
    if 'language' not in st.session_state:
        st.session_state.language = 'pl'

    load_navbar_css()

    # Get current page from query params
    try:
        query_params = st.query_params
        current_page = query_params.get("page", "")
    except AttributeError:
        # Fallback for older Streamlit versions
        query_params = st.experimental_get_query_params()
        current_page = query_params.get("page", [""])[0]

    # Determine navigation links based on current page
    if current_page == "testowanie_oprogramowania":
        home_link = "?"
        features_link = "?"
        analytics_link = "?"
        about_link = "?"
        contact_link = "?"
    else:
        home_link = "#home"
        features_link = "#features"
        analytics_link = "#analytics"
        about_link = "#about"
        contact_link = "#contact"

    # Navigation will be handled by pure JavaScript event listeners

    st.markdown(f"""
    <div class="sticky-navbar">
        <div class="navbar-content">
            <div class="menu-items">
                <div class="logo"><span class="chip-icon"></span> aIRONick</div>
                <a href="{home_link}" class="menu-link smooth-scroll" id="menu-home" data-section="home">{t('navbar.home')}</a>
                <a href="{features_link}" class="menu-link smooth-scroll" id="menu-features" data-section="features">{t('navbar.software_testing')}</a>
                <a href="{analytics_link}" class="menu-link smooth-scroll" id="menu-analytics" data-section="analytics">{t('navbar.electrician')}</a>
                <a href="{about_link}" class="menu-link smooth-scroll" id="menu-about" data-section="about">{t('navbar.youtube')}</a>
                <a href="{contact_link}" class="menu-link smooth-scroll" id="menu-contact" data-section="contact">{t('navbar.contact')}</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # NAJPROSTSZE ROZWIĄZANIE - tylko CSS smooth scroll
    st.markdown("""
    <script>
    // Minimal working solution
    document.addEventListener('DOMContentLoaded', function() {
        console.log('🚀 Simple navbar script loading...');
        
        // Simple scroll to section function
        function scrollToSection(sectionId) {
            const element = document.getElementById(sectionId);
            if (element) {
                element.scrollIntoView({ behavior: 'smooth', block: 'start' });
                return true;
            }
            return false;
        }
        
        // Add click handlers to all menu links
        const menuLinks = document.querySelectorAll('.menu-link[data-section]');
        menuLinks.forEach(function(link) {
            const section = link.getAttribute('data-section');
            if (section) {
                link.addEventListener('click', function(e) {
                    e.preventDefault();
                    scrollToSection(section);
                });
            }
        });
        
        // Make globally available
        window.scrollToSection = scrollToSection;
        console.log('✅ Simple navbar ready!');
    });
    </script>
    """, unsafe_allow_html=True)

    # Language dropdown integrated into navbar
    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

    with col4:
        current_display = "🇵🇱 Polski" if st.session_state.language == 'pl' else "🇬🇧 English"
        selected = st.selectbox(
            "",
            list(LANGUAGE_OPTIONS.keys()),
            index=0 if st.session_state.language == 'pl' else 1,
            key="language_selector",
            label_visibility="collapsed"
        )

        new_lang = LANGUAGE_OPTIONS[selected]
        if new_lang != st.session_state.language:
            st.session_state.language = new_lang
            st.rerun()