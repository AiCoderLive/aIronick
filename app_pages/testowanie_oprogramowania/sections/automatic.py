import streamlit as st
from translations.loader import t


def create_automatic_testing_section():
    st.header(t("software_testing.automatic.title"))

    st.write(t("software_testing.automatic.description"))

    st.subheader(t("software_testing.automatic.services_title"))

    st.write(t("software_testing.automatic.integration_tests"))
    st.write(t("software_testing.automatic.end_to_end_tests"))
    st.write(t("software_testing.automatic.api_tests"))
    st.write(t("software_testing.automatic.regression_tests"))
    st.write(t("software_testing.automatic.smoke_tests"))

    st.subheader(t("software_testing.automatic.technologies_title"))

    st.write(t("software_testing.automatic.selenium"))
    st.write(t("software_testing.automatic.playwright"))
    st.write(t("software_testing.automatic.pytest"))
    st.write(t("software_testing.automatic.testng_junit"))
    st.write(t("software_testing.automatic.postman"))
    st.write(t("software_testing.automatic.docker"))

    st.subheader(t("software_testing.automatic.benefits_title"))

    st.write(t("software_testing.automatic.benefits_intro"))

    st.write(t("software_testing.automatic.faster_detection"))
    st.write(t("software_testing.automatic.cost_reduction"))
    st.write(t("software_testing.automatic.better_quality"))
    st.write(t("software_testing.automatic.continuous_integration"))
    st.write(t("software_testing.automatic.maximum_coverage"))
