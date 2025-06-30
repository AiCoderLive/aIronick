import streamlit as st
from config.constants import LANGUAGE_OPTIONS
from translations.loader import t
from styles.navbar import load_navbar_css
from utils.url_helper import URLHelper

def create_navbar():
    """Create and display the main navigation bar"""
    if 'language' not in st.session_state:
        st.session_state.language = 'pl'

    load_navbar_css()

    # Get current page from query params using URLHelper
    current_page = URLHelper.get_page_param()
    
    # Determine navigation links based on current page
    home_url = URLHelper.get_home_url()
    if current_page == "testowanie_oprogramowania":
        home_link = home_url
        features_link = home_url
        analytics_link = home_url
        about_link = home_url
        contact_link = home_url
    else:
        home_link = "#home"
        features_link = "#features"
        analytics_link = "#analytics"
        about_link = "#about"
        contact_link = "#contact"
    
    # Create onclick handlers - prevent default link behavior and use JavaScript navigation
    if current_page != 'testowanie_oprogramowania':
        home_onclick = "event.preventDefault(); scrollToSection('home'); return false;"
        features_onclick = "event.preventDefault(); scrollToSection('features'); return false;"
        analytics_onclick = "event.preventDefault(); scrollToSection('analytics'); return false;"
        about_onclick = "event.preventDefault(); scrollToSection('about'); return false;"
        contact_onclick = "event.preventDefault(); scrollToSection('contact'); return false;"
    else:
        home_onclick = f"window.location.href='{home_url}'"
        features_onclick = f"window.location.href='{home_url}'"
        analytics_onclick = f"window.location.href='{home_url}'"
        about_onclick = f"window.location.href='{home_url}'"
        contact_onclick = f"window.location.href='{home_url}'"
    
    st.markdown(f"""
    <div class="sticky-navbar">
        <div class="navbar-content">
            <div class="menu-items">
                <div class="logo"><span class="chip-icon"></span> aIRONick</div>
                <a href="{home_link}" class="menu-link" id="menu-home" onclick="{home_onclick}">{t('navbar.home')}</a>
                <a href="{features_link}" class="menu-link" id="menu-features" onclick="{features_onclick}">{t('navbar.software_testing')}</a>
                <a href="{analytics_link}" class="menu-link" id="menu-analytics" onclick="{analytics_onclick}">{t('navbar.electrician')}</a>
                <a href="{about_link}" class="menu-link" id="menu-about" onclick="{about_onclick}">{t('navbar.youtube')}</a>
                <a href="{contact_link}" class="menu-link" id="menu-contact" onclick="{contact_onclick}">{t('navbar.contact')}</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Add JavaScript with proper timing and error handling
    st.markdown("""
    <script>
    // Wait for DOM to be fully loaded
    document.addEventListener('DOMContentLoaded', function() {
        initializeNavbar();
    });
    
    // Also try after a short delay to ensure Streamlit components are ready
    setTimeout(initializeNavbar, 500);
    
    function initializeNavbar() {
        // Define scroll function with error handling
        window.scrollToSection = function(sectionId) {
            setTimeout(function() {
                const element = document.getElementById(sectionId);
                if (element) {
                    element.scrollIntoView({ 
                        behavior: 'smooth', 
                        block: 'start',
                        inline: 'nearest'
                    });
                } else {
                    console.warn('Section not found:', sectionId);
                    // Fallback: try to scroll to approximate position
                    const fallbackPositions = {
                        'home': 0,
                        'features': 800,
                        'analytics': 1600,
                        'about': 2400,
                        'contact': 3200
                    };
                    if (fallbackPositions[sectionId]) {
                        window.scrollTo({
                            top: fallbackPositions[sectionId],
                            behavior: 'smooth'
                        });
                    }
                }
            }, 100);
        };

        // Highlight active menu item based on scroll position
        function updateActiveMenu() {
            const sections = ['home', 'features', 'analytics', 'about', 'contact'];
            let activeFound = false;

            sections.forEach(section => {
                const element = document.getElementById(section);
                const menuLink = document.getElementById('menu-' + section);

                if (element && menuLink && !activeFound) {
                    const rect = element.getBoundingClientRect();
                    const isInView = rect.top <= 150 && rect.bottom >= 100;

                    if (isInView) {
                        // Remove active class from all menu items
                        document.querySelectorAll('.menu-link').forEach(link => {
                            link.classList.remove('active');
                        });
                        // Add active class to current menu item
                        menuLink.classList.add('active');
                        activeFound = true;
                    }
                }
            });
        }

        // Update active menu on scroll with throttling
        let scrollTimeout;
        window.addEventListener('scroll', function() {
            if (scrollTimeout) {
                clearTimeout(scrollTimeout);
            }
            scrollTimeout = setTimeout(updateActiveMenu, 50);
        });
        
        // Initial update
        updateActiveMenu();
    }
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