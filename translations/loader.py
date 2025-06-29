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
        },
        "software_testing": {
            "automatic": {
                "title": "🤖 Testowanie Automatyczne",
                "description": "Automatyzacja testów to klucz do efektywnego rozwoju oprogramowania. Oferujemy kompleksowe rozwiązania automatyzacji, które przyspieszają proces testowania i zwiększają pokrycie testami.",
                "services_title": "🔧 Nasze Usługi Automatyzacji",
                "integration_tests": "**Testy integracyjne:** Weryfikacja współpracy między modułami",
                "end_to_end_tests": "**Testy end-to-end:** Kompleksowe scenariusze użytkowania",
                "api_tests": "**Testy API:** Automatyzacja testów interfejsów REST",
                "regression_tests": "**Testy regresyjne:** Ciągła weryfikacja stabilności aplikacji",
                "smoke_tests": "**Testy smoke:** Szybka weryfikacja kluczowych funkcjonalności",
                "technologies_title": "🛠️ Technologie i Narzędzia",
                "selenium": "**Selenium WebDriver:** Automatyzacja przeglądarek internetowych",
                "playwright": "**Playwright:** Cross-browser testing",
                "pytest": "**PyTest:** Testy w języku Python",
                "testng_junit": "**TestNG/JUnit:** Testy w ekosystemie Java",
                "postman": "**Postman:** Automatyzacja testów API",
                "docker": "**Docker:** Konteneryzacja środowisk testowych",
                "benefits_title": "📈 Korzyści z Automatyzacji",
                "benefits_intro": "Automatyzacja testów pozwala na:",
                "faster_detection": "**Szybsze względem manualnego wykrywanie błędów:** Natychmiastowe informowanie o problemach",
                "cost_reduction": "**Redukcja kosztów:** Mniejsze nakłady na ręczne testowanie",
                "better_quality": "**Lepsza jakość:** Consistentne i powtarzalne testy",
                "continuous_integration": "**Ciągła integracja:** Integracja z pipeline'ami CI/CD",
                "maximum_coverage": "**Największe pokrycie:** Możliwość testowania dużej ilości scenariuszy"
            },
            "performance": {
                "title": "⚡ Testowanie Wydajnościowe",
                "description": "Wydajność aplikacji to kluczowy czynnik sukcesu. Przeprowadzamy kompleksowe testy wydajnościowe, które pozwalają zoptymalizować działanie Twojej aplikacji pod różnymi obciążeniami.",
                "types_title": "📊 Rodzaje Testów Wydajnościowych",
                "load_testing": "**Load Testing:** Testowanie pod normalnym obciążeniem użytkowników",
                "stress_testing": "**Stress Testing:** Testowanie pod ekstremalnym obciążeniem",
                "spike_testing": "**Spike Testing:** Testowanie nagłych wzrostów ruchu",
                "volume_testing": "**Volume Testing:** Testowanie z dużymi ilościami danych",
                "endurance_testing": "**Endurance Testing:** Długotrwałe testy stabilności",
                "scalability_testing": "**Scalability Testing:** Testowanie skalowalności systemu",
                "tools_title": "🛠️ Narzędzia i Technologie",
                "gatling": "**Gatling:** Wysokowydajne testy obciążenia",
                "jmeter": "**JMeter:** Wszechstronne narzędzie do testów obciążenia",
                "loadrunner": "**LoadRunner:** Zaawansowane testy enterprise",
                "monitoring": "**Dynatrace/Datadog/Elastic Search:** Monitoring aplikacji",
                "visualization": "**Grafana/Prometheus:** Wizualizacja metryk wydajności",
                "metrics_title": "📈 Kluczowe Metryki",
                "metrics_intro": "Podczas testów wydajnościowych analizujemy:",
                "response_time": "**Response Time:** Czas odpowiedzi aplikacji",
                "throughput": "**Throughput:** Liczba transakcji na sekundę",
                "concurrent_users": "**Concurrent Users:** Liczba jednoczesnych użytkowników",
                "error_rate": "**Error Rate:** Procent błędnych odpowiedzi",
                "resource_utilization": "**Resource Utilization:** Wykorzystanie CPU, RAM, dysku",
                "database_performance": "**Database Performance:** Wydajność bazy danych",
                "process_title": "🎯 Proces Testowania",
                "process_intro": "Nasz proces obejmuje:",
                "requirements_analysis": "**Analiza wymagań:** Określenie celów wydajnościowych",
                "test_planning": "**Planowanie testów:** Przygotowanie scenariuszy testowych",
                "environment_preparation": "**Przygotowanie środowiska:** Konfiguracja narzędzi testowych",
                "test_execution": "**Wykonanie testów:** Przeprowadzenie testów obciążenia",
                "results_analysis": "**Analiza wyników:** Szczegółowa analiza metryk",
                "recommendations": "**Rekomendacje:** Propozycje optymalizacji"
            },
            "overview": {
                "title": "📋 Przegląd Usług Testowania Oprogramowania",
                "description": "Oferujemy kompleksowe usługi testowania oprogramowania, które zapewniają najwyższą jakość Twoich aplikacji. Nasze doświadczenie obejmuje różnorodne technologie i platformy.",
                "specializations_title": "🎯 Nasze Specjalizacje",
                "functional_testing": "**Testowanie funkcjonalne:** Weryfikacja zgodności aplikacji z wymaganiami biznesowymi",
                "automated_testing": "**Testowanie automatyczne:** Efektywne testy regresyjne i ciągła integracja",
                "performance_testing": "**Testowanie wydajnościowe:** Analiza wydajności pod obciążeniem",
                "security_testing": "**Testowanie bezpieczeństwa:** Wykrywanie podatności i luk bezpieczeństwa",
                "mobile_testing": "**Testowanie mobilne:** Aplikacje iOS i Android",
                "api_testing": "**Testowanie API:** Weryfikacja interfejsów programistycznych",
                "why_choose_title": "💼 Dlaczego Warto Wybrać Nas?",
                "why_choose_description": "Posiadamy wieloletnie doświadczenie w branży IT, nowoczesne narzędzia oraz zespół certyfikowanych testerów. Każdy projekt traktujemy indywidualnie."
            }
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
        },
        "software_testing": {
            "automatic": {
                "title": "🤖 Automated Testing",
                "description": "Test automation is the key to efficient software development. We offer comprehensive automation solutions that accelerate the testing process and increase test coverage.",
                "services_title": "🔧 Our Automation Services",
                "integration_tests": "**Integration Tests:** Verification of cooperation between modules",
                "end_to_end_tests": "**End-to-End Tests:** Comprehensive usage scenarios",
                "api_tests": "**API Tests:** REST interface testing automation",
                "regression_tests": "**Regression Tests:** Continuous verification of application stability",
                "smoke_tests": "**Smoke Tests:** Quick verification of key functionalities",
                "technologies_title": "🛠️ Technologies and Tools",
                "selenium": "**Selenium WebDriver:** Web browser automation",
                "playwright": "**Playwright:** Cross-browser testing",
                "pytest": "**PyTest:** Python testing framework",
                "testng_junit": "**TestNG/JUnit:** Java ecosystem testing",
                "postman": "**Postman:** API testing automation",
                "docker": "**Docker:** Test environment containerization",
                "benefits_title": "📈 Benefits of Automation",
                "benefits_intro": "Test automation allows for:",
                "faster_detection": "**Faster error detection compared to manual:** Immediate problem notifications",
                "cost_reduction": "**Cost reduction:** Lower manual testing overhead",
                "better_quality": "**Better quality:** Consistent and repeatable tests",
                "continuous_integration": "**Continuous integration:** Integration with CI/CD pipelines",
                "maximum_coverage": "**Maximum coverage:** Ability to test a large number of scenarios"
            },
            "performance": {
                "title": "⚡ Performance Testing",
                "description": "Application performance is a key success factor. We conduct comprehensive performance tests that allow optimization of your application under various loads.",
                "types_title": "📊 Types of Performance Tests",
                "load_testing": "**Load Testing:** Testing under normal user load",
                "stress_testing": "**Stress Testing:** Testing under extreme load",
                "spike_testing": "**Spike Testing:** Testing sudden traffic spikes",
                "volume_testing": "**Volume Testing:** Testing with large amounts of data",
                "endurance_testing": "**Endurance Testing:** Long-term stability tests",
                "scalability_testing": "**Scalability Testing:** System scalability testing",
                "tools_title": "🛠️ Tools and Technologies",
                "gatling": "**Gatling:** High-performance load testing",
                "jmeter": "**JMeter:** Versatile load testing tool",
                "loadrunner": "**LoadRunner:** Advanced enterprise testing",
                "monitoring": "**Dynatrace/Datadog/Elastic Search:** Application monitoring",
                "visualization": "**Grafana/Prometheus:** Performance metrics visualization",
                "metrics_title": "📈 Key Metrics",
                "metrics_intro": "During performance testing we analyze:",
                "response_time": "**Response Time:** Application response time",
                "throughput": "**Throughput:** Transactions per second",
                "concurrent_users": "**Concurrent Users:** Number of simultaneous users",
                "error_rate": "**Error Rate:** Percentage of error responses",
                "resource_utilization": "**Resource Utilization:** CPU, RAM, disk usage",
                "database_performance": "**Database Performance:** Database performance",
                "process_title": "🎯 Testing Process",
                "process_intro": "Our process includes:",
                "requirements_analysis": "**Requirements analysis:** Defining performance goals",
                "test_planning": "**Test planning:** Preparing test scenarios",
                "environment_preparation": "**Environment preparation:** Testing tools configuration",
                "test_execution": "**Test execution:** Conducting load tests",
                "results_analysis": "**Results analysis:** Detailed metrics analysis",
                "recommendations": "**Recommendations:** Optimization proposals"
            },
            "overview": {
                "title": "📋 Software Testing Services Overview",
                "description": "We offer comprehensive software testing services that ensure the highest quality of your applications. Our experience covers diverse technologies and platforms.",
                "specializations_title": "🎯 Our Specializations",
                "functional_testing": "**Functional testing:** Verification of application compliance with business requirements",
                "automated_testing": "**Automated testing:** Efficient regression tests and continuous integration",
                "performance_testing": "**Performance testing:** Performance analysis under load",
                "security_testing": "**Security testing:** Detection of vulnerabilities and security gaps",
                "mobile_testing": "**Mobile testing:** iOS and Android applications",
                "api_testing": "**API testing:** Verification of programming interfaces",
                "why_choose_title": "💼 Why Choose Us?",
                "why_choose_description": "We have years of experience in the IT industry, modern tools and a team of certified testers. We treat each project individually."
            }
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