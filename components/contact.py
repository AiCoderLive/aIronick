import streamlit as st
from translations.loader import t
from config.constants import CONTACT_INFO

def create_contact_section():
    """Create and display the contact section"""
    st.markdown(f"""
    <div class="section" id="contact" style="padding-top: 100px;">
        <h2 class="section-title">{t('contact.title')}</h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="card">
            <h3>{t('contact.get_in_touch')}</h3>
            <p>📧 {t('contact.email')}: {CONTACT_INFO["email"]}</p>
            <p>📱 {t('contact.phone')}: {CONTACT_INFO["phone"]}</p>
            <p>🌐 {t('contact.website')}: {CONTACT_INFO["website"]}</p>
            <p>📍 {t('contact.service_area')}: {t('contact.service_area_value')}</p>
            <p>⏰ {t('contact.hours')}: {t('contact.hours_value')}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader(t('contact.send_message'))

        with st.form("contact_form"):
            name = st.text_input(t('contact.your_name'))
            email = st.text_input(t('contact.email_address'))
            service = st.selectbox(t('contact.service_needed'), [
                t('contact.software_testing'),
                t('contact.hardware_testing'),
                t('contact.electrical_services'),
                t('contact.gaming_solutions'),
                t('contact.multiple_services'),
                t('contact.consultation')
            ])
            message = st.text_area(t('contact.project_details'), height=100,
                                   placeholder=t('contact.project_placeholder'))

            if st.form_submit_button(t('contact.request_quote')):
                if name and email and message:
                    st.success(t('contact.success_message'))
                else:
                    st.error(t('contact.error_message'))

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)