import streamlit as st
import os
from urllib.parse import urljoin, urlparse

class URLHelper:
    """Helper class for consistent URL generation across different deployment environments"""
    
    @staticmethod
    def get_base_url():
        """Get the base URL for the application"""
        # Try to get from environment variable first (for production)
        base_url = os.getenv('STREAMLIT_BASE_URL', '')
        
        # Try to get from Streamlit config
        if not base_url:
            try:
                base_url = st.get_option("server.baseUrlPath") or ""
            except:
                base_url = ""
        
        # Ensure base_url starts with / if not empty
        if base_url and not base_url.startswith('/'):
            base_url = '/' + base_url
            
        return base_url
    
    @staticmethod
    def get_home_url():
        """Get the URL for the home page"""
        base_url = URLHelper.get_base_url()
        if base_url:
            return base_url + "/"
        return "?"
    
    @staticmethod
    def get_page_url(page_name):
        """Get the URL for a specific page"""
        base_url = URLHelper.get_base_url()
        if base_url:
            return f"{base_url}/?page={page_name}"
        return f"?page={page_name}"
    
    @staticmethod
    def set_query_params_safe(**params):
        """Safely set query parameters with fallback for older Streamlit versions"""
        try:
            for key, value in params.items():
                st.query_params[key] = value
        except AttributeError:
            # Fallback for older Streamlit versions
            st.experimental_set_query_params(**params)
    
    @staticmethod
    def get_query_params_safe():
        """Safely get query parameters with fallback for older Streamlit versions"""
        try:
            return dict(st.query_params)
        except AttributeError:
            # Fallback for older Streamlit versions
            params = st.experimental_get_query_params()
            # Convert list values to single values
            return {k: v[0] if isinstance(v, list) and v else v for k, v in params.items()}
    
    @staticmethod
    def get_page_param():
        """Get the current page parameter"""
        params = URLHelper.get_query_params_safe()
        return params.get("page", "")
    
    @staticmethod
    def navigate_to_page(page_name):
        """Navigate to a specific page"""
        URLHelper.set_query_params_safe(page=page_name)
        st.rerun()
    
    @staticmethod
    def navigate_to_home():
        """Navigate to home page"""
        try:
            st.query_params.clear()
        except AttributeError:
            st.experimental_set_query_params()
        st.rerun()