import streamlit as st

def load_base_css():
    """Load base CSS styles for the application"""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global container with responsive max-width */
    .main .block-container {
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1200px !important;
        margin: 0 auto !important;
    }

    :root {
        --primary: #2563eb;
        --primary-hover: #1d4ed8;
        --primary-light: #3b82f6;
        --secondary: #64748b;
        --accent: #059669;
        --surface: #ffffff;
        --surface-alt: #f8fafc;
        --background: #ffffff;
        --text-primary: #1e293b;
        --text-secondary: #64748b;
        --text-muted: #94a3b8;
        --border: #e2e8f0;
        --border-light: #f1f5f9;
        --shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
        --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    }

    * {
        box-sizing: border-box;
    }

    html {
        scroll-behavior: smooth;
    }
    
    /* Ensure smooth scrolling works for all anchor links */
    .smooth-scroll {
        scroll-behavior: smooth;
    }
    
    /* Fix scroll position for fixed navbar */
    section[id], div[id] {
        scroll-margin-top: 80px;
    }

    /* Remove default link styling everywhere */
    a {
        text-decoration: none !important;
    }
    
    a:hover,
    a:focus,
    a:active,
    a:visited {
        text-decoration: none !important;
    }
    
    /* Ensure buttons are fully clickable */
    .menu-link * {
        pointer-events: none;
    }
    
    .menu-link {
        pointer-events: auto;
    }

    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        line-height: 1.6;
        color: var(--text-primary);
    }

    .main > div {
        padding-top: 0rem;
    }

    .stApp {
        background: var(--background);
        color: var(--text-primary);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    .stApp > header {
        background-color: transparent;
    }

    /* Clean, Professional Buttons */
    .stButton > button {
        background: var(--primary);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 6px;
        font-weight: 500;
        font-size: 0.875rem;
        transition: all 0.15s ease;
        font-family: inherit;
        box-shadow: var(--shadow);
    }

    .stButton > button:hover {
        background: var(--primary-hover);
        box-shadow: var(--shadow-md);
        transform: translateY(-1px);
    }

    .stButton > button:active {
        transform: translateY(0);
        box-shadow: var(--shadow);
    }

    /* Clean Input Styles */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > div {
        background: var(--surface);
        color: var(--text-primary);
        border: 1px solid var(--border);
        border-radius: 6px;
        font-family: inherit;
        transition: border-color 0.15s ease;
        font-size: 0.875rem;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > div:focus {
        border-color: var(--primary);
        outline: none;
        box-shadow: 0 0 0 3px rgb(37 99 235 / 0.1);
    }

    /* Mobile styles */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }

        .hero-section {
            padding: 6rem 1rem 4rem 1rem;
        }

        .section {
            padding: 3rem 1rem;
        }

        .feature-grid {
            grid-template-columns: 1fr;
        }
        
        .main .block-container {
            max-width: none !important;
            margin-left: 0 !important;
        }
    }

    /* Large screen optimizations */
    @media (min-width: 1200px) {
        .hero-section {
            max-width: 1400px;
            margin: 0 auto;
            padding: 8rem 2rem 6rem 2rem;
        }

        .section {
            max-width: 1400px;
            margin: 0 auto;
            padding: 4rem 2rem;
        }
        
        .hero-title {
            font-size: 4rem;
            max-width: 800px;
            line-height: 1.1;
        }
        
        .hero-subtitle {
            font-size: 1.3rem;
            max-width: 700px;
        }
    }

    /* Ultra-wide screen optimizations */
    @media (min-width: 1600px) {
        .hero-section {
            padding: 10rem 3rem 8rem 3rem;
        }
        
        .section {
            padding: 5rem 3rem;
        }
        
        .feature-grid {
            grid-template-columns: repeat(3, minmax(320px, 400px));
            justify-content: center;
            gap: 2rem;
            max-width: 1300px;
            margin: 3rem auto;
        }
    }
    </style>
    """, unsafe_allow_html=True)