import streamlit as st

def create_overview_section():
    def create_overview_section():
        st.header("📋 Przegląd Usług Testowania Oprogramowania")

        st.write(
            "Oferujemy kompleksowe usługi testowania oprogramowania, które zapewniają najwyższą jakość Twoich aplikacji. Nasze doświadczenie obejmuje różnorodne technologie i platformy.")

        st.subheader("🎯 Nasze Specjalizacje")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Testowanie funkcjonalne:** Weryfikacja zgodności aplikacji z wymaganiami biznesowymi")
            st.write("**Testowanie automatyczne:** Efektywne testy regresyjne i ciągła integracja")
            st.write("**Testowanie wydajnościowe:** Analiza wydajności pod obciążeniem")

        with col2:
            st.write("**Testowanie bezpieczeństwa:** Wykrywanie podatności i luk bezpieczeństwa")
            st.write("**Testowanie mobilne:** Aplikacje iOS i Android")
            st.write("**Testowanie API:** Weryfikacja interfejsów programistycznych")

        st.subheader("💼 Dlaczego Warto Wybrać Nas?")
        st.write(
            "Posiadamy wieloletnie doświadczenie w branży IT, nowoczesne narzędzia oraz zespół certyfikowanych testerów. Każdy projekt traktujemy indywidualnie.")