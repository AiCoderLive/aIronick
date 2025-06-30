import streamlit as st
from config.page_config import setup_page_config, initialize_language
from app_pages.home import show_home_page
from app_pages.testowanie_oprogramowania.main import show_testing_page
from utils.url_helper import URLHelper

def main():
    # Handle page routing first to determine sidebar state
    page = URLHelper.get_page_param()
    
    # Configure page based on current page
    if page == "testowanie_oprogramowania":
        setup_page_config(sidebar_state="expanded")
    else:
        # For home page, don't initialize sidebar at all
        st.set_page_config(
            page_title="aIRONick",
            page_icon="💻",
            layout="wide"
        )
    
    initialize_language()
    
    if page == "testowanie_oprogramowania":
        show_testing_page()
    else:
        show_home_page()

if __name__ == "__main__":
    main()