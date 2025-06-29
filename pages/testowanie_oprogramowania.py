import streamlit as st
import sys
import os

# Add parent directory to path to import from main app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import load_translations, get_translation, t, create_navbar

st.set_page_config(
    page_title="aIRONick - Testowanie Oprogramowania",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize language in session state
if 'language' not in st.session_state:
    st.session_state.language = 'pl'

def load_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
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
        --shadow: rgba(0, 0, 0, 0.1);
        --shadow-hover: rgba(0, 0, 0, 0.15);
    }

    .stApp {
        background: var(--background);
        color: var(--text-primary);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: var(--surface);
        border-right: 1px solid var(--border);
    }

    /* Main content area */
    .main-content {
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
        padding-top: 100px; /* Account for fixed top navbar */
    }

    .page-header {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 3rem 2rem;
        text-align: center;
        border-radius: 12px;
        margin-bottom: 3rem;
        box-shadow: 0 2px 8px var(--shadow);
    }

    .page-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 1rem;
    }

    .page-subtitle {
        font-size: 1.1rem;
        color: var(--text-secondary);
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }

    .section {
        background: var(--surface);
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 2px 8px var(--shadow);
        border: 1px solid var(--border);
    }

    .section h2 {
        color: var(--text-primary);
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid var(--primary);
        padding-bottom: 0.5rem;
    }

    .section h3 {
        color: var(--text-primary);
        font-size: 1.3rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
    }

    .section p {
        color: var(--text-secondary);
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    .feature-list {
        list-style: none;
        padding: 0;
    }

    .feature-list li {
        background: var(--background);
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        border-left: 4px solid var(--primary);
        transition: all 0.2s ease;
    }

    .feature-list li:hover {
        transform: translateX(5px);
        box-shadow: 0 2px 8px var(--shadow);
    }

    .feature-list li strong {
        color: var(--text-primary);
    }

    .back-button {
        background: var(--primary);
        color: white;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.2s ease;
        display: inline-block;
        margin-bottom: 2rem;
    }

    .back-button:hover {
        background: var(--primary-hover);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(26, 115, 232, 0.3);
        color: white;
        text-decoration: none;
    }

    /* Sidebar menu styling */
    .sidebar-menu {
        background: var(--surface);
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px var(--shadow);
    }

    .menu-item {
        display: block;
        padding: 0.75rem 1rem;
        color: var(--text-secondary);
        text-decoration: none;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        font-weight: 500;
        transition: all 0.2s ease;
        cursor: pointer;
    }

    .menu-item:hover {
        background: rgba(26, 115, 232, 0.1);
        color: var(--primary);
        transform: translateX(5px);
    }

    .menu-item.active {
        background: var(--primary);
        color: white;
    }

    /* Hide Streamlit sidebar default styling */
    .css-1d391kg {
        padding: 1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

def create_sidebar():
    with st.sidebar:
        st.markdown("### 🔧 Testowanie Oprogramowania")
        
        # Language selector
        language_options = {"🇵🇱 Polski": "pl", "🇬🇧 English": "en"}
        current_display = "🇵🇱 Polski" if st.session_state.language == 'pl' else "🇬🇧 English"
        selected = st.selectbox(
            "Język / Language",
            list(language_options.keys()),
            index=0 if st.session_state.language == 'pl' else 1,
            key="language_selector"
        )
        
        new_lang = language_options[selected]
        if new_lang != st.session_state.language:
            st.session_state.language = new_lang
            st.rerun()
        
        st.markdown("---")
        
        # Navigation menu
        if 'selected_section' not in st.session_state:
            st.session_state.selected_section = 'overview'
        
        menu_items = {
            'overview': '📋 Przegląd' if st.session_state.language == 'pl' else '📋 Overview',
            'automatic': '🤖 Testowanie automatyczne' if st.session_state.language == 'pl' else '🤖 Automatic Testing',
            'performance': '⚡ Testowanie wydajnościowe' if st.session_state.language == 'pl' else '⚡ Performance Testing'
        }
        
        for key, label in menu_items.items():
            if st.button(label, key=f"menu_{key}", use_container_width=True):
                st.session_state.selected_section = key
                st.rerun()

def create_overview_section():
    st.markdown("""
    <div class="section">
        <h2>📋 Przegląd Usług Testowania Oprogramowania</h2>
        <p>Oferujemy kompleksowe usługi testowania oprogramowania, które zapewniają najwyższą jakość Twoich aplikacji. Nasze doświadczenie obejmuje różnorodne technologie i platformy.</p>
        
        <h3>🎯 Nasze Specjalizacje</h3>
        <ul class="feature-list">
            <li><strong>Testowanie funkcjonalne:</strong> Weryfikacja zgodności aplikacji z wymaganiami biznesowymi</li>
            <li><strong>Testowanie automatyczne:</strong> Efektywne testy regresyjne i ciągła integracja</li>
            <li><strong>Testowanie wydajnościowe:</strong> Analiza wydajności pod obciążeniem</li>
            <li><strong>Testowanie bezpieczeństwa:</strong> Wykrywanie podatności i luk bezpieczeństwa</li>
            <li><strong>Testowanie mobilne:</strong> Aplikacje iOS i Android</li>
            <li><strong>Testowanie API:</strong> Weryfikacja interfejsów programistycznych</li>
        </ul>
        
        <h3>💼 Dlaczego Warto Wybrać Nas?</h3>
        <p>Posiadamy wieloletnie doświadczenie w branży IT, nowoczesne narzędzia oraz zespół certyfikowanych testerów. Każdy projekt traktujemy indywidualnie, dostosowując metody testowania do specyfiki Twojej aplikacji.</p>
    </div>
    """, unsafe_allow_html=True)

def create_automatic_testing_section():
    st.markdown("""
    <div class="section">
        <h2>🤖 Testowanie Automatyczne</h2>
        <p>Automatyzacja testów to klucz do efektywnego rozwoju oprogramowania. Oferujemy kompleksowe rozwiązania automatyzacji, które przyspieszają proces testowania i zwiększają pokrycie testami.</p>
        
        <h3>🔧 Nasze Usługi Automatyzacji</h3>
        <ul class="feature-list">
            <li><strong>Testy jednostkowe (Unit Tests):</strong> Testowanie pojedynczych komponentów aplikacji</li>
            <li><strong>Testy integracyjne:</strong> Weryfikacja współpracy między modułami</li>
            <li><strong>Testy end-to-end:</strong> Kompleksowe scenariusze użytkowania</li>
            <li><strong>Testy API:</strong> Automatyzacja testów interfejsów REST/GraphQL</li>
            <li><strong>Testy regresyjne:</strong> Ciągła weryfikacja stabilności aplikacji</li>
            <li><strong>Testy smoke:</strong> Szybka weryfikacja kluczowych funkcjonalności</li>
        </ul>
        
        <h3>🛠️ Technologie i Narzędzia</h3>
        <ul class="feature-list">
            <li><strong>Selenium WebDriver:</strong> Automatyzacja przeglądarek internetowych</li>
            <li><strong>Cypress:</strong> Nowoczesne testy front-endowe</li>
            <li><strong>Playwright:</strong> Cross-browser testing</li>
            <li><strong>Jest/Mocha:</strong> Frameworki do testów JavaScript</li>
            <li><strong>PyTest:</strong> Testy w języku Python</li>
            <li><strong>TestNG/JUnit:</strong> Testy w ekosystemie Java</li>
            <li><strong>Postman/Newman:</strong> Automatyzacja testów API</li>
            <li><strong>Docker:</strong> Konteneryzacja środowisk testowych</li>
        </ul>
        
        <h3>📈 Korzyści z Automatyzacji</h3>
        <p>Automatyzacja testów pozwala na:</p>
        <ul class="feature-list">
            <li><strong>Szybsze wykrywanie błędów:</strong> Natychmiastowe informowanie o problemach</li>
            <li><strong>Redukcja kosztów:</strong> Mniejsze nakłady na ręczne testowanie</li>
            <li><strong>Lepsza jakość:</strong> Consistentne i powtarzalne testy</li>
            <li><strong>Ciągła integracja:</strong> Integracja z pipeline'ami CI/CD</li>
            <li><strong>Większe pokrycie:</strong> Możliwość testowania więcej scenariuszy</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def create_performance_testing_section():
    st.markdown("""
    <div class="section">
        <h2>⚡ Testowanie Wydajnościowe</h2>
        <p>Wydajność aplikacji to kluczowy czynnik sukcesu. Przeprowadzamy kompleksowe testy wydajnościowe, które pozwalają zoptymalizować działanie Twojej aplikacji pod różnymi obciążeniami.</p>
        
        <h3>📊 Rodzaje Testów Wydajnościowych</h3>
        <ul class="feature-list">
            <li><strong>Load Testing:</strong> Testowanie pod normalnym obciążeniem użytkowników</li>
            <li><strong>Stress Testing:</strong> Testowanie pod ekstremalnym obciążeniem</li>
            <li><strong>Spike Testing:</strong> Testowanie nagłych wzrostów ruchu</li>
            <li><strong>Volume Testing:</strong> Testowanie z dużymi ilościami danych</li>
            <li><strong>Endurance Testing:</strong> Długotrwałe testy stabilności</li>
            <li><strong>Scalability Testing:</strong> Testowanie skalowalności systemu</li>
        </ul>
        
        <h3>🛠️ Narzędzia i Technologie</h3>
        <ul class="feature-list">
            <li><strong>JMeter:</strong> Wszechstronne narzędzie do testów obciążenia</li>
            <li><strong>K6:</strong> Nowoczesne testy wydajności JavaScript</li>
            <li><strong>Artillery:</strong> Testy obciążenia API i aplikacji web</li>
            <li><strong>LoadRunner:</strong> Zaawansowane testy enterprise</li>
            <li><strong>Gatling:</strong> Wysokowydajne testy obciążenia</li>
            <li><strong>New Relic/Datadog:</strong> Monitoring aplikacji</li>
            <li><strong>Grafana/Prometheus:</strong> Wizualizacja metryk wydajności</li>
        </ul>
        
        <h3>📈 Kluczowe Metryki</h3>
        <p>Podczas testów wydajnościowych analizujemy:</p>
        <ul class="feature-list">
            <li><strong>Response Time:</strong> Czas odpowiedzi aplikacji</li>
            <li><strong>Throughput:</strong> Liczba transakcji na sekundę</li>
            <li><strong>Concurrent Users:</strong> Liczba jednoczesnych użytkowników</li>
            <li><strong>Error Rate:</strong> Procent błędnych odpowiedzi</li>
            <li><strong>Resource Utilization:</strong> Wykorzystanie CPU, RAM, dysku</li>
            <li><strong>Database Performance:</strong> Wydajność bazy danych</li>
        </ul>
        
        <h3>🎯 Proces Testowania</h3>
        <p>Nasz proces obejmuje:</p>
        <ul class="feature-list">
            <li><strong>Analiza wymagań:</strong> Określenie celów wydajnościowych</li>
            <li><strong>Planowanie testów:</strong> Przygotowanie scenariuszy testowych</li>
            <li><strong>Przygotowanie środowiska:</strong> Konfiguracja narzędzi testowych</li>
            <li><strong>Wykonanie testów:</strong> Przeprowadzenie testów obciążenia</li>
            <li><strong>Analiza wyników:</strong> Szczegółowa analiza metryk</li>
            <li><strong>Rekomendacje:</strong> Propozycje optymalizacji</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


def show_testowanie_oprogramowania_page():
    """Function to display the testowanie oprogramowania page content"""
    load_custom_css()
    
    create_sidebar()
    
    # Main content wrapper with top padding
    st.markdown('<div style="padding-top: 100px;">', unsafe_allow_html=True)
    
    # Back button
    st.markdown('<a href="?" class="back-button">← Powrót do strony głównej</a>', unsafe_allow_html=True)
    
    # Page header
    st.markdown("""
    <div class="page-header">
        <h1 class="page-title">🔧 Testowanie Oprogramowania</h1>
        <p class="page-subtitle">Profesjonalne usługi testowania oprogramowania - automatyzacja, wydajność, jakość</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Main content based on selected section
    if st.session_state.selected_section == 'overview':
        create_overview_section()
    elif st.session_state.selected_section == 'automatic':
        create_automatic_testing_section()
    elif st.session_state.selected_section == 'performance':
        create_performance_testing_section()

def main():
    load_custom_css()
    
    # Add top navigation menu
    create_navbar()
    
    show_testowanie_oprogramowania_page()

if __name__ == "__main__":
    main()