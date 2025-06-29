import streamlit as st

def create_performance_testing_section():
    """Create performance testing section"""
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