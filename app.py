import streamlit as st
from config.page_config import setup_page_config, initialize_language
from app_pages.home import show_home_page
from app_pages.testowanie_oprogramowania.main import show_testing_page

def main():
    # Handle page routing first to determine sidebar state
    try:
        query_params = st.query_params
        page = query_params.get("page", "")
    except AttributeError:
        # Fallback for older Streamlit versions
        query_params = st.experimental_get_query_params()
        page = query_params.get("page", [""])[0]
    
    # Configure page based on current page
    if page == "testowanie_oprogramowania":
        setup_page_config(sidebar_state="expanded")
    else:
        # For home page, don't initialize sidebar at all
        st.set_page_config(
            page_title="aIRONick",
            page_icon="⚙️",
            layout="wide"
        )
    
    initialize_language()
    
    if page == "testowanie_oprogramowania":
        show_testing_page()
    else:
        show_home_page()

if __name__ == "__main__":
    main()