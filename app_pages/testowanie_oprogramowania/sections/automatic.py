import streamlit as st

def create_automatic_testing_section():
    """Create automatic testing section"""
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