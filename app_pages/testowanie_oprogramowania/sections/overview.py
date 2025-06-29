import streamlit as st
from translations.loader import t

def create_overview_section():
    st.header(t("software_testing.overview.title"))

    st.write(t("software_testing.overview.description"))

    st.subheader(t("software_testing.overview.specializations_title"))

    col1, col2 = st.columns(2)

    with col1:
        st.write(t("software_testing.overview.functional_testing"))
        st.write(t("software_testing.overview.automated_testing"))
        st.write(t("software_testing.overview.performance_testing"))

    with col2:
        st.write(t("software_testing.overview.security_testing"))
        st.write(t("software_testing.overview.mobile_testing"))
        st.write(t("software_testing.overview.api_testing"))

    st.subheader(t("software_testing.overview.why_choose_title"))
    st.write(t("software_testing.overview.why_choose_description"))