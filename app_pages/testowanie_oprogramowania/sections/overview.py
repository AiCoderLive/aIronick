import streamlit as st

def create_overview_section():
    """Create overview section for testing page"""
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