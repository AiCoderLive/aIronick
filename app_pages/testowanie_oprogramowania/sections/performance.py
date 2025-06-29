import streamlit as st
from translations.loader import t


def create_performance_testing_section():
    """Create performance testing section"""
    st.header(t("software_testing.performance.title"))

    st.write(t("software_testing.performance.description"))

    st.subheader(t("software_testing.performance.types_title"))

    st.write(t("software_testing.performance.load_testing"))
    st.write(t("software_testing.performance.stress_testing"))
    st.write(t("software_testing.performance.spike_testing"))
    st.write(t("software_testing.performance.volume_testing"))
    st.write(t("software_testing.performance.endurance_testing"))
    st.write(t("software_testing.performance.scalability_testing"))

    st.subheader(t("software_testing.performance.tools_title"))

    st.write(t("software_testing.performance.gatling"))
    st.write(t("software_testing.performance.jmeter"))
    st.write(t("software_testing.performance.loadrunner"))
    st.write(t("software_testing.performance.monitoring"))
    st.write(t("software_testing.performance.visualization"))

    st.subheader(t("software_testing.performance.metrics_title"))

    st.write(t("software_testing.performance.metrics_intro"))

    st.write(t("software_testing.performance.response_time"))
    st.write(t("software_testing.performance.throughput"))
    st.write(t("software_testing.performance.concurrent_users"))
    st.write(t("software_testing.performance.error_rate"))
    st.write(t("software_testing.performance.resource_utilization"))
    st.write(t("software_testing.performance.database_performance"))

    st.subheader(t("software_testing.performance.process_title"))

    st.write(t("software_testing.performance.process_intro"))

    st.write(t("software_testing.performance.requirements_analysis"))
    st.write(t("software_testing.performance.test_planning"))
    st.write(t("software_testing.performance.environment_preparation"))
    st.write(t("software_testing.performance.test_execution"))
    st.write(t("software_testing.performance.results_analysis"))
    st.write(t("software_testing.performance.recommendations"))