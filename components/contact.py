import streamlit as st
from translations.loader import t
from config.constants import CONTACT_INFO

def create_contact_section():
    """Create and display the contact section using pure Streamlit"""
        
    # Contact section
    st.markdown("---")
    st.markdown("## " + t('contact.title'))

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### " + t('contact.get_in_touch'))
        st.markdown(f"📧 **{t('contact.email')}:** {CONTACT_INFO['email']}")
        st.markdown(f"📱 **{t('contact.phone')}:** {CONTACT_INFO['phone']}")
        st.markdown(f"🌐 **{t('contact.website')}:** {CONTACT_INFO['website']}")
        st.markdown(f"📍 **{t('contact.service_area')}:** {t('contact.service_area_value')}")
        st.markdown(f"⏰ **{t('contact.hours')}:** {t('contact.hours_value')}")

    with col2:
        st.markdown("### " + t('contact.send_message'))

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

            if st.form_submit_button(t('contact.request_quote'), use_container_width=True):
                if name and email and message:
                    st.success(t('contact.success_message'))
                else:
                    st.error(t('contact.error_message'))