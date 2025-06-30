import streamlit as st

def load_base_css():
    """Load base CSS styles for the application"""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&display=swap');
    
    /* Global container with responsive max-width */
    .main .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 1400px !important;
        margin: 0 auto !important;
    }

    :root {
        --primary: #1a73e8;
        --primary-hover: #1557b0;
        --secondary: #5f6368;
        --surface: #ffffff;
        --background: #fafafa;
        --text-primary: #202124;
        --text-secondary: #5f6368;
        --border: #dadce0;
        --border-hover: #9aa0a6;
        --matrix-green: #00ff41;
        --shadow: rgba(0, 0, 0, 0.1);
        --shadow-hover: rgba(0, 0, 0, 0.15);
    }

    * {
        box-sizing: border-box;
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

    .stButton > button {
        background: var(--primary);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.2s ease;
        font-size: 0.9rem;
    }

    .stButton > button:hover {
        background: var(--primary-hover);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(26, 115, 232, 0.3);
    }

    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: var(--surface);
        color: var(--text-primary);
        border: 1px solid var(--border);
        border-radius: 8px;
        font-family: inherit;
        transition: border-color 0.2s ease;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--primary);
        box-shadow: 0 0 0 3px rgba(26, 115, 232, 0.1);
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