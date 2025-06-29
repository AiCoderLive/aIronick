import streamlit as st
import json
import os

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