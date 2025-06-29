import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json
import os

st.set_page_config(
    page_title="aIRONick",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize language in session state
if 'language' not in st.session_state:
    st.session_state.language = 'pl'


@st.cache_data
def load_translations():
    """Load translation files"""
    translations = {}

    # Polish translations
    translations['pl'] = {
        "navbar": {
            "home": "Strona główna",
            "software_testing": "Testowanie oprogramowania",
            "electrician": "Elektryk",
            "youtube": "YouTube",
            "contact": "Kontakt"
        },
        "hero": {
            "title": "Profesjonalne Rozwiązania Testowe i Gamingowe",
            "subtitle": "Odkryj świat najnowszych technologii wspieranych sztuczną inteligencją! Specjalizujemy się w automatycznym testowaniu oprogramowania, testach wydajności oraz elektryce i elektronice. Regularnie publikujemy na YouTube testy elementów elektronicznych, filmy instruktażowe z lutowania, materiały z rozgrywek i inne zagadnienia techniczne. Dołącz do naszej społeczności pasjonatów – rozwijaj swoje umiejętności i bądź na bieżąco z innowacjami!",
            "cta_button": "Nasze Usługi"
        },
        "features": {
            "title": "Testowanie oprogramowania",
            "software_testing": {
                "title": "Testowanie Oprogramowania",
                "description": "Kompleksowe usługi automatyzacji testów, testowania wydajności i zapewniania jakości. Zapewniamy, że Twoje aplikacje działają bezawaryjnie na wszystkich platformach i środowiskach."
            },
            "gaming_solutions": {
                "title": "Rozwiązania Gamingowe",
                "description": "Profesjonalne konfiguracje gamingowe, instalacje konsol, budowa PC do gier i optymalizacja wydajności zarówno dla konkurencyjnych, jak i casualowych doświadczeń gamingowych."
            },
            "hardware_testing": {
                "title": "Testowanie Sprzętu",
                "description": "Profesjonalna diagnostyka sprzętu, testowanie komponentów i walidacja systemów. Od serwerów po elektronikę użytkową, zapewniamy optymalną wydajność i niezawodność."
            },
            "electrical_services": {
                "title": "Usługi Elektryczne",
                "description": "Licencjonowane prace elektryczne, w tym instalacje, naprawy, okablowanie i diagnostyka systemów elektrycznych. Rozwiązania elektryczne certyfikowane pod kątem bezpieczeństwa i zgodne z przepisami."
            }
        },
        "electrician": {
            "title": "Elektryka",
            "residential": {
                "title": "Instalacje Mieszkaniowe",
                "description": "Kompleksowe usługi elektryczne dla domów, w tym okablowanie, instalacja gniazdek, modernizacja tablic, wentylatory sufitowe, oprawy oświetleniowe i naprawy elektryczne. Licencjonowani i ubezpieczeni dla Twojego bezpieczeństwa."
            },
            "commercial": {
                "title": "Instalacje Komercyjne",
                "description": "Profesjonalne prace elektryczne dla firm, biur i obiektów przemysłowych. Awaryjne usługi elektryczne, kontrakty na konserwację i kontrole zgodności z przepisami."
            },
            "troubleshooting": {
                "title": "Rozwiązywanie Problemów Elektrycznych",
                "description": "Ekspercka diagnoza i naprawa problemów elektrycznych. Problemy z wyłącznikami, awarie zasilania, wykrywanie wadliwego okablowania i kontrole bezpieczeństwa elektrycznego przy użyciu zaawansowanego sprzętu testowego."
            },
            "smart_home": {
                "title": "Instalacje Smart Home",
                "description": "Nowoczesne rozwiązania elektryczne dla inteligentnych domów, w tym inteligentne przełączniki, gniazdka, systemy automatyki domowej, stacje ładowania EV i energooszczędne instalacje oświetlenia LED."
            }
        },
        "youtube": {
            "title": "YouTube",
            "watch_videos": "Obejrzyj nasze najnowsze filmy",
            "description": "Sprawdź nasz kanał YouTube, aby obejrzeć tutoriale, materiały zza kulis i techniczne spostrzeżenia. Subskrybuj, aby być na bieżąco z naszymi najnowszymi treściami!",
            "visit_channel": "Odwiedź nasz kanał YouTube",
            "featured_playlists": "Wyróżnione Playlisty",
            "playlist_software_testing": "Testowanie Oprogramowania",
            "playlist_software_testing_desc": "Kompleksowe tutoriale dotyczące automatyzacji testów, testowania wydajności i najlepszych praktyk QA",
            "playlist_gaming_tech": "Technologie Gamingowe",
            "playlist_gaming_tech_desc": "Konfiguracje gamingowe, recenzje sprzętu i przewodniki optymalizacji wydajności",
            "playlist_electrical_work": "Prace Elektryczne",
            "playlist_electrical_work_desc": "Demonstracje bezpieczeństwa, przewodniki instalacji i wskazówki dotyczące rozwiązywania problemów",
            "playlist_hardware_reviews": "Recenzje Sprzętu",
            "playlist_hardware_reviews_desc": "Dogłębne testowanie sprzętu, diagnostyka i recenzje komponentów",
            "watch_playlist": "Zobacz Playlistę"
        },
        "contact": {
            "title": "Gotowy do rozpoczęcia?",
            "get_in_touch": "Skontaktuj się z nami",
            "email": "Email",
            "phone": "Telefon",
            "website": "Strona",
            "service_area": "Obszar usług",
            "service_area_value": "Większy obszar metropolitalny",
            "hours": "Godziny",
            "hours_value": "Pon-Pt 9:00-18:00, Usługi awaryjne dostępne",
            "send_message": "Wyślij nam wiadomość",
            "your_name": "Twoje imię",
            "email_address": "Adres email",
            "service_needed": "Potrzebna usługa",
            "software_testing": "Testowanie oprogramowania",
            "hardware_testing": "Testowanie sprzętu",
            "electrical_services": "Usługi elektryczne",
            "gaming_solutions": "Rozwiązania gamingowe",
            "multiple_services": "Wiele usług",
            "consultation": "Konsultacja",
            "project_details": "Szczegóły projektu",
            "project_placeholder": "Opisz wymagania swojego projektu...",
            "request_quote": "Poproś o wycenę",
            "success_message": "Dziękujemy! Przedstawimy szczegółową wycenę w ciągu 24 godzin.",
            "error_message": "Proszę wypełnić wszystkie pola."
        },
        "footer": {
            "copyright": "© 2024 aIRONick Technical Services. Licencjonowani i ubezpieczeni.",
            "services": "Testowanie oprogramowania • Testowanie sprzętu • Usługi elektryczne • Rozwiązania gamingowe"
        }
    }

    # English translations
    translations['en'] = {
        "navbar": {
            "home": "Home",
            "software_testing": "Software testing",
            "electrician": "Electrician",
            "youtube": "Youtube",
            "contact": "Contact"
        },
        "hero": {
            "title": "Professional Testing & Gaming Solutions",
            "subtitle": "Discover the world of cutting-edge technologies powered by artificial intelligence! We specialize in automated software testing, performance testing, and electrical & electronics. We regularly publish electronic component tests, soldering tutorials, gameplay videos and other technical topics on YouTube. Join our community of enthusiasts – develop your skills and stay up to date with innovations!",
            "cta_button": "Our Services"
        },
        "features": {
            "title": "Software testing",
            "software_testing": {
                "title": "Software Testing",
                "description": "Comprehensive automation testing, performance testing, and quality assurance services. We ensure your applications run flawlessly across all platforms and environments."
            },
            "gaming_solutions": {
                "title": "Gaming Solutions",
                "description": "Professional gaming setups, console installations, gaming PC builds, and performance optimization for both competitive and casual gaming experiences."
            },
            "hardware_testing": {
                "title": "Hardware Testing",
                "description": "Professional hardware diagnostics, component testing, and system validation. From servers to consumer electronics, we ensure optimal performance and reliability."
            },
            "electrical_services": {
                "title": "Electrical Services",
                "description": "Licensed electrical work including installations, repairs, wiring, and electrical system diagnostics. Safety-certified and code-compliant electrical solutions."
            }
        },
        "electrician": {
            "title": "Electrician",
            "residential": {
                "title": "Residential Electrical",
                "description": "Complete home electrical services including wiring, outlet installation, panel upgrades, ceiling fans, lighting fixtures, and electrical repairs. Licensed and insured for your safety."
            },
            "commercial": {
                "title": "Commercial Electrical",
                "description": "Professional commercial electrical work for businesses, offices, and industrial facilities. Emergency electrical services, maintenance contracts, and code compliance inspections."
            },
            "troubleshooting": {
                "title": "Electrical Troubleshooting",
                "description": "Expert diagnosis and repair of electrical problems. Circuit breaker issues, power outages, faulty wiring detection, and electrical safety inspections using advanced testing equipment."
            },
            "smart_home": {
                "title": "Smart Home Installation",
                "description": "Modern smart home electrical solutions including smart switches, outlets, home automation systems, EV charging stations, and energy-efficient LED lighting installations."
            }
        },
        "youtube": {
            "title": "YouTube",
            "watch_videos": "Watch Our Latest Videos",
            "description": "Check out our YouTube channel for tutorials, behind-the-scenes content, and tech insights. Subscribe to stay updated with our latest content!",
            "visit_channel": "Visit Our YouTube Channel",
            "featured_playlists": "Featured Playlists",
            "playlist_software_testing": "Software Testing",
            "playlist_software_testing_desc": "Comprehensive tutorials on automated testing, performance testing, and QA best practices",
            "playlist_gaming_tech": "Gaming Tech",
            "playlist_gaming_tech_desc": "Gaming setups, hardware reviews, and performance optimization guides",
            "playlist_electrical_work": "Electrical Work",
            "playlist_electrical_work_desc": "Safety demonstrations, installation guides, and troubleshooting tips",
            "playlist_hardware_reviews": "Hardware Reviews",
            "playlist_hardware_reviews_desc": "In-depth hardware testing, diagnostics, and component reviews",
            "watch_playlist": "Watch Playlist"
        },
        "contact": {
            "title": "Ready to get started?",
            "get_in_touch": "Get in Touch",
            "email": "Email",
            "phone": "Phone",
            "website": "Website",
            "service_area": "Service Area",
            "service_area_value": "Greater Metro Area",
            "hours": "Hours",
            "hours_value": "Mon-Fri 9AM-6PM, Emergency services available",
            "send_message": "Send us a message",
            "your_name": "Your Name",
            "email_address": "Email Address",
            "service_needed": "Service Needed",
            "software_testing": "Software Testing",
            "hardware_testing": "Hardware Testing",
            "electrical_services": "Electrical Services",
            "gaming_solutions": "Gaming Solutions",
            "multiple_services": "Multiple Services",
            "consultation": "Consultation",
            "project_details": "Project Details",
            "project_placeholder": "Describe your project requirements...",
            "request_quote": "Request Quote",
            "success_message": "Thank you! We'll provide a detailed quote within 24 hours.",
            "error_message": "Please fill in all fields."
        },
        "footer": {
            "copyright": "© 2024 aIRONick Technical Services. Licensed & Insured.",
            "services": "Software Testing • Hardware Testing • Electrical Services • Gaming Solutions"
        }
    }

    return translations


def get_translation(key, lang=None):
    """Get translation for a key with support for nested keys like 'section.key'"""
    if lang is None:
        lang = st.session_state.language

    translations = load_translations()

    if lang not in translations:
        return key

    # Handle nested keys
    keys = key.split('.')
    value = translations[lang]

    try:
        for k in keys:
            value = value[k]
        return value
    except (KeyError, TypeError):
        return key


def t(key):
    """Shorthand for get_translation"""
    return get_translation(key)


def load_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&display=swap');

    :root {
        --primary: #1a73e8;
        --primary-hover: #1557b0;
        --secondary: #5f6368;
        --surface: #ffffff;
        --background: #fafafa;
        --text-primary: #202124;
        --text-secondary: #5f6368;
        --border: #dadce0;
        --border-hover: #9aa0a6;
        --matrix-green: #00ff41;
        --shadow: rgba(0, 0, 0, 0.1);
        --shadow-hover: rgba(0, 0, 0, 0.15);
    }

    * {
        box-sizing: border-box;
    }

    .main > div {
        padding-top: 0rem;
    }

    .stApp {
        background: var(--background);
        color: var(--text-primary);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    .stApp > header {
        background-color: transparent;
    }

    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid var(--border);
        padding: 1rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 1px 6px var(--shadow);
    }

    .navbar-brand {
        font-family: 'Orbitron', monospace;
        font-size: 1.5rem;
        font-weight: 900;
        color: var(--matrix-green);
        text-decoration: none;
        text-shadow: 0 0 8px rgba(0, 255, 65, 0.3);
        letter-spacing: 1px;
        animation: matrix-glow 3s ease-in-out infinite;
    }

    @keyframes matrix-glow {
        0%, 100% { text-shadow: 0 0 8px rgba(0, 255, 65, 0.3); }
        50% { text-shadow: 0 0 16px rgba(0, 255, 65, 0.6), 0 0 24px rgba(0, 255, 65, 0.4); }
    }

    .navbar-nav {
        display: flex;
        list-style: none;
        margin: 0;
        padding: 0;
        gap: 0;
    }

    .nav-link {
        color: var(--text-secondary);
        text-decoration: none;
        font-weight: 400;
        transition: all 0.2s ease;
        padding: 0.75rem 1.25rem;
        border-radius: 8px;
        font-size: 0.9rem;
    }

    .nav-link:hover {
        color: var(--primary);
        background: rgba(26, 115, 232, 0.08);
    }

    .hero-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        color: var(--text-primary);
        padding: 8rem 2rem 5rem 2rem;
        text-align: center;
        margin-top: 0;
    }

    .hero-title {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        color: var(--text-primary);
        line-height: 1.1;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        margin-bottom: 2rem;
        color: var(--text-secondary);
        font-weight: 400;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.5;
    }

    .section {
        padding: 5rem 2rem;
        margin: 0;
        background: var(--surface);
    }

    .section:nth-child(even) {
        background: var(--background);
    }

    .section-title {
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 3rem;
        color: var(--text-primary);
        font-weight: 600;
        line-height: 1.2;
    }

    .card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 2px 8px var(--shadow);
        margin-bottom: 1.5rem;
        transition: all 0.2s ease;
    }

    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px var(--shadow-hover);
        border-color: var(--border-hover);
    }

    .card h3 {
        color: var(--text-primary);
        font-weight: 600;
        font-size: 1.25rem;
        margin-bottom: 1rem;
        line-height: 1.3;
    }

    .card p {
        color: var(--text-secondary);
        line-height: 1.6;
        font-size: 0.95rem;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }

    .metric-card {
        background: var(--surface);
        color: var(--text-primary);
        padding: 2rem;
        border: 1px solid var(--border);
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 2px 8px var(--shadow);
        transition: all 0.2s ease;
    }

    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px var(--shadow-hover);
    }

    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: var(--primary);
    }

    .metric-label {
        font-size: 0.9rem;
        color: var(--text-secondary);
        font-weight: 500;
    }

    .footer {
        background: var(--surface);
        color: var(--text-secondary);
        padding: 3rem 2rem;
        text-align: center;
        border-top: 1px solid var(--border);
        font-size: 0.9rem;
    }

    .stButton > button {
        background: var(--primary);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.2s ease;
        font-size: 0.9rem;
    }

    .stButton > button:hover {
        background: var(--primary-hover);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(26, 115, 232, 0.3);
    }

    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: var(--surface);
        color: var(--text-primary);
        border: 1px solid var(--border);
        border-radius: 8px;
        font-family: inherit;
        transition: border-color 0.2s ease;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--primary);
        box-shadow: 0 0 0 3px rgba(26, 115, 232, 0.1);
    }

    .cta-button {
        display: inline-block;
        background: var(--primary);
        color: white;
        padding: 1rem 2rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.2s ease;
        margin-top: 1rem;
    }

    .cta-button:hover {
        background: var(--primary-hover);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(26, 115, 232, 0.3);
    }

    /* Language selector styles */
    .language-selector {
        position: fixed;
        top: 15px;
        right: 30px;
        z-index: 1000;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 8px;
    }

    .language-btn {
        background: transparent;
        border: none;
        padding: 8px 12px;
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.2s ease;
        font-size: 14px;
        margin: 0 2px;
    }

    .language-btn:hover {
        background: rgba(26, 115, 232, 0.1);
    }

    .language-btn.active {
        background: var(--primary);
        color: white;
    }

    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            padding: 1rem;
        }

        .navbar-nav {
            margin-top: 1rem;
            flex-wrap: wrap;
            justify-content: center;
            gap: 0.25rem;
        }

        .hero-title {
            font-size: 2.5rem;
        }

        .hero-section {
            padding: 6rem 1rem 4rem 1rem;
        }

        .section {
            padding: 3rem 1rem;
        }

        .feature-grid {
            grid-template-columns: 1fr;
        }

        .language-selector {
            top: 10px;
            right: 10px;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def create_navbar():
    if 'language' not in st.session_state:
        st.session_state.language = 'pl'

    # Sticky navbar CSS and JavaScript
    st.markdown(f"""
    <style>
    .sticky-navbar {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid #dadce0;
        padding: 15px 30px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }}
    .navbar-content {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
    }}
    .menu-items {{
        display: flex;
        align-items: center;
        gap: 30px;
    }}
    .menu-link {{
        text-decoration: none;
        color: #5f6368;
        font-weight: 400;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        padding: 8px 16px;
        border-radius: 8px;
    }}
    .menu-link:hover {{
        color: #1f77b4;
        background: rgba(31, 119, 180, 0.1);
    }}
    .menu-link.active {{
        color: #1f77b4;
        background: rgba(31, 119, 180, 0.15);
        border-bottom: 2px solid #1f77b4;
    }}
    .logo {{
        font-weight: bold;
        font-size: 2rem;
        color: #00ff41;
    }}
    body {{
        padding-top: 80px;
    }}
    </style>
    """, unsafe_allow_html=True)

    # Main navbar with translated menu items
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
    
    # Create onclick handlers without backslashes in f-string
    home_onclick = "scrollToSection('home')" if current_page != 'testowanie_oprogramowania' else "window.location.href='?'"
    features_onclick = "scrollToSection('features')" if current_page != 'testowanie_oprogramowania' else "window.location.href='?'"
    analytics_onclick = "scrollToSection('analytics')" if current_page != 'testowanie_oprogramowania' else "window.location.href='?'"
    about_onclick = "scrollToSection('about')" if current_page != 'testowanie_oprogramowania' else "window.location.href='?'"
    contact_onclick = "scrollToSection('contact')" if current_page != 'testowanie_oprogramowania' else "window.location.href='?'"
    
    st.markdown(f"""
    <div class="sticky-navbar">
        <div class="navbar-content">
            <div class="menu-items">
                <div class="logo">🤖 aIRONick</div>
                <a href="{home_link}" class="menu-link" id="menu-home" onclick="{home_onclick}">{t('navbar.home')}</a>
                <a href="{features_link}" class="menu-link" id="menu-features" onclick="{features_onclick}">{t('navbar.software_testing')}</a>
                <a href="{analytics_link}" class="menu-link" id="menu-analytics" onclick="{analytics_onclick}">{t('navbar.electrician')}</a>
                <a href="{about_link}" class="menu-link" id="menu-about" onclick="{about_onclick}">{t('navbar.youtube')}</a>
                <a href="{contact_link}" class="menu-link" id="menu-contact" onclick="{contact_onclick}">{t('navbar.contact')}</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Add JavaScript separately
    st.markdown("""
    <script>
    function scrollToSection(sectionId) {
        const element = document.getElementById(sectionId);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }

    // Highlight active menu item based on scroll position
    function updateActiveMenu() {
        const sections = ['home', 'features', 'analytics', 'about', 'contact'];

        sections.forEach(section => {
            const element = document.getElementById(section);
            const menuLink = document.getElementById('menu-' + section);

            if (element && menuLink) {
                const rect = element.getBoundingClientRect();
                const isInView = rect.top <= 100 && rect.bottom >= 100;

                if (isInView) {
                    // Remove active class from all menu items
                    document.querySelectorAll('.menu-link').forEach(link => {
                        link.classList.remove('active');
                    });
                    // Add active class to current menu item
                    menuLink.classList.add('active');
                }
            }
        });
    }

    // Update active menu on scroll
    window.addEventListener('scroll', updateActiveMenu);
    // Update active menu on load
    window.addEventListener('load', updateActiveMenu);
    </script>
    """, unsafe_allow_html=True)

    # Language dropdown integrated into navbar
    language_options = {"🇵🇱 Polski": "pl", "🇬🇧 English": "en"}

    # Hide the selectbox but keep it functional
    st.markdown("""
    <style>
    .language-dropdown {
        position: fixed;
        top: 25px;
        right: 30px;
        z-index: 1000;
    }

    .language-dropdown select {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border: 1px solid #dadce0;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 14px;
        color: #5f6368;
        cursor: pointer;
        transition: all 0.2s ease;
        outline: none;
    }

    .language-dropdown select:hover {
        border-color: #1a73e8;
        box-shadow: 0 2px 8px rgba(26, 115, 232, 0.2);
    }

    .language-dropdown select:focus {
        border-color: #1a73e8;
        box-shadow: 0 0 0 3px rgba(26, 115, 232, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

    # Create the language dropdown
    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

    with col4:
        current_display = "🇵🇱 Polski" if st.session_state.language == 'pl' else "🇬🇧 English"
        selected = st.selectbox(
            "",
            list(language_options.keys()),
            index=0 if st.session_state.language == 'pl' else 1,
            key="language_selector",
            label_visibility="collapsed"
        )

        new_lang = language_options[selected]
        if new_lang != st.session_state.language:
            st.session_state.language = new_lang
            st.rerun()

    # Position the dropdown in the navbar area
    st.markdown("""
    <style>
    /* Move the selectbox to navbar position */
    div[data-testid="column"]:nth-child(4) > div > div > div[data-testid="stSelectbox"] {
        position: fixed !important;
        top: 25px !important;
        right: 30px !important;
        z-index: 1000 !important;
        width: auto !important;
        min-width: 120px !important;
    }

    div[data-testid="column"]:nth-child(4) > div > div > div[data-testid="stSelectbox"] > div > div {
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid #dadce0 !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
    }

    div[data-testid="column"]:nth-child(4) > div > div > div[data-testid="stSelectbox"] select {
        background: transparent !important;
        color: #5f6368 !important;
        font-size: 14px !important;
        padding: 8px 12px !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)


def create_hero_section():
    st.markdown(f"""
    <div class="hero-section" id="home" style="padding-top: 120px;">
        <h1 class="hero-title">{t('hero.title')}</h1>
        <p class="hero-subtitle">{t('hero.subtitle')}</p>
    </div>
    """, unsafe_allow_html=True)


def create_features_section():
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
        
        <div style="text-align: center; margin-top: 2.5rem;">
            <a href="?page=testowanie_oprogramowania" style="
                background: var(--primary);
                color: white;
                padding: 1rem 2.5rem;
                border-radius: 8px;
                text-decoration: none;
                font-weight: 600;
                font-size: 1.1rem;
                transition: all 0.3s ease;
                display: inline-block;
                box-shadow: 0 4px 12px rgba(26, 115, 232, 0.3);
            ">
                📋 Zobacz więcej
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)


def create_analytics_section():
    st.markdown(f"""
    <div class="section" id="analytics">
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


def create_about_section():
    st.markdown(f"""
    <div class="section" id="about">
        <h2 class="section-title">{t('youtube.title')}</h2>
    """, unsafe_allow_html=True)

    st.markdown(f"### 🎥 {t('youtube.watch_videos')}")
    st.write(t('youtube.description'))

    # Create centered button using Streamlit
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(f"🚀 {t('youtube.visit_channel')}", key="youtube_btn"):
            st.markdown('<meta http-equiv="refresh" content="0; url=https://www.youtube.com/@aIrOnick">',
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
            <a href="https://www.youtube.com/@aIrOnick/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ {t('youtube.watch_playlist')}</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="card" style="text-align: center;">
            <h4>🎮 {t('youtube.playlist_gaming_tech')}</h4>
            <p>{t('youtube.playlist_gaming_tech_desc')}</p>
            <a href="https://www.youtube.com/@aIrOnick/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ {t('youtube.watch_playlist')}</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card" style="text-align: center;">
            <h4>⚡ {t('youtube.playlist_electrical_work')}</h4>
            <p>{t('youtube.playlist_electrical_work_desc')}</p>
            <a href="https://www.youtube.com/@aIrOnick/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ {t('youtube.watch_playlist')}</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="card" style="text-align: center;">
            <h4>💻 {t('youtube.playlist_hardware_reviews')}</h4>
            <p>{t('youtube.playlist_hardware_reviews_desc')}</p>
            <a href="https://www.youtube.com/@aIrOnick/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ {t('youtube.watch_playlist')}</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


def create_contact_section():
    st.markdown(f"""
    <div class="section" id="contact">
        <h2 class="section-title">{t('contact.title')}</h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="card">
            <h3>{t('contact.get_in_touch')}</h3>
            <p>📧 {t('contact.email')}: kontakt@aironick.com</p>
            <p>📱 {t('contact.phone')}: +48 730 379 623</p>
            <p>🌐 {t('contact.website')}: www.aironick.com</p>
            <p>📍 {t('contact.service_area')}: {t('contact.service_area_value')}</p>
            <p>⏰ {t('contact.hours')}: {t('contact.hours_value')}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader(t('contact.send_message'))

        with st.form("contact_form"):
            name = st.text_input(t('contact.your_name'))
            email = st.text_input(t('contact.email_address'))
            service = st.selectbox(t('contact.service_needed'), [
                t('contact.software_testing'),
                t('contact.hardware_testing'),
                t('contact.electrical_services'),
                t('contact.gaming_solutions'),
                t('contact.multiple_services'),
                t('contact.consultation')
            ])
            message = st.text_area(t('contact.project_details'), height=100,
                                   placeholder=t('contact.project_placeholder'))

            if st.form_submit_button(t('contact.request_quote')):
                if name and email and message:
                    st.success(t('contact.success_message'))
                else:
                    st.error(t('contact.error_message'))

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


def create_footer():
    st.markdown(f"""
    <div class="footer">
        <p>{t('footer.copyright')}</p>
        <p>{t('footer.services')}</p>
    </div>
    """, unsafe_allow_html=True)


def main():
    load_custom_css()
    create_navbar()
    
    # Handle page routing
    query_params = st.experimental_get_query_params()
    page = query_params.get("page", [""])[0]
    
    if page == "testowanie_oprogramowania":
        # Import and show the testowanie_oprogramowania page
        import sys
        import os
        sys.path.append(os.path.join(os.path.dirname(__file__), 'pages'))
        
        try:
            from testowanie_oprogramowania import show_testowanie_oprogramowania_page
            show_testowanie_oprogramowania_page()
        except ImportError:
            st.error("Strona 'Testowanie oprogramowania' nie została znaleziona.")
    else:
        # Show main page content
        create_hero_section()
        create_features_section()
        create_analytics_section()
        create_about_section()
        create_contact_section()
        create_footer()


if __name__ == "__main__":
    main()