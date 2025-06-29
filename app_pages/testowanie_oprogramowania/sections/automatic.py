import streamlit as st


def create_automatic_testing_section():
    st.header("🤖 Testowanie Automatyczne")

    st.write(
        "Automatyzacja testów to klucz do efektywnego rozwoju oprogramowania. Oferujemy kompleksowe rozwiązania automatyzacji, które przyspieszają proces testowania i zwiększają pokrycie testami.")

    st.subheader("🔧 Nasze Usługi Automatyzacji")

    st.write("**Testy integracyjne:** Weryfikacja współpracy między modułami")
    st.write("**Testy end-to-end:** Kompleksowe scenariusze użytkowania")
    st.write("**Testy API:** Automatyzacja testów interfejsów REST")
    st.write("**Testy regresyjne:** Ciągła weryfikacja stabilności aplikacji")
    st.write("**Testy smoke:** Szybka weryfikacja kluczowych funkcjonalności")

    st.subheader("🛠️ Technologie i Narzędzia")

    st.write("**Selenium WebDriver:** Automatyzacja przeglądarek internetowych")
    st.write("**Playwright:** Cross-browser testing")
    st.write("**PyTest:** Testy w języku Python")
    st.write("**TestNG/JUnit:** Testy w ekosystemie Java")
    st.write("**Postman:** Automatyzacja testów API")
    st.write("**Docker:** Konteneryzacja środowisk testowych")

    st.subheader("📈 Korzyści z Automatyzacji")

    st.write("Automatyzacja testów pozwala na:")

    st.write("**Szybsze wzgledem manualnego wykrywanie błędów:** Natychmiastowe informowanie o problemach")
    st.write("**Redukcja kosztów:** Mniejsze nakłady na ręczne testowanie")
    st.write("**Lepsza jakość:** Consistentne i powtarzalne testy")
    st.write("**Ciągła integracja:** Integracja z pipeline'ami CI/CD")
    st.write("**Największe pokrycie:** Możliwość testowania duzej scenariuszy")
