import streamlit as st

def load_testing_page_css():
    """Load CSS styles for testing page"""
    st.markdown("""
    <style>
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: var(--surface);
        border-right: 1px solid var(--border);
    }

    /* Main content area */
    .main-content {
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
        padding-top: 100px; /* Account for fixed top navbar */
    }

    .page-header {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 3rem 2rem;
        text-align: center;
        border-radius: 12px;
        margin-bottom: 3rem;
        box-shadow: 0 2px 8px var(--shadow);
    }

    .page-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 1rem;
    }

    .page-subtitle {
        font-size: 1.1rem;
        color: var(--text-secondary);
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }

    .section {
        background: var(--surface);
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 2px 8px var(--shadow);
        border: 1px solid var(--border);
    }

    .section h2 {
        color: var(--text-primary);
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid var(--primary);
        padding-bottom: 0.5rem;
    }

    .section h3 {
        color: var(--text-primary);
        font-size: 1.3rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
    }

    .section p {
        color: var(--text-secondary);
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    .feature-list {
        list-style: none;
        padding: 0;
    }

    .feature-list li {
        background: var(--background);
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        border-left: 4px solid var(--primary);
        transition: all 0.2s ease;
    }

    .feature-list li:hover {
        transform: translateX(5px);
        box-shadow: 0 2px 8px var(--shadow);
    }

    .feature-list li strong {
        color: var(--text-primary);
    }

    .back-button {
        background: var(--primary);
        color: white;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.2s ease;
        display: inline-block;
        margin-bottom: 2rem;
    }

    .back-button:hover {
        background: var(--primary-hover);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(26, 115, 232, 0.3);
        color: white;
        text-decoration: none;
    }

    /* Sidebar menu styling */
    .sidebar-menu {
        background: var(--surface);
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px var(--shadow);
    }

    .menu-item {
        display: block;
        padding: 0.75rem 1rem;
        color: var(--text-secondary);
        text-decoration: none;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        font-weight: 500;
        transition: all 0.2s ease;
        cursor: pointer;
    }

    .menu-item:hover {
        background: rgba(26, 115, 232, 0.1);
        color: var(--primary);
        transform: translateX(5px);
    }

    .menu-item.active {
        background: var(--primary);
        color: white;
    }

    /* Hide Streamlit sidebar default styling */
    .css-1d391kg {
        padding: 1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)