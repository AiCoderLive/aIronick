import streamlit as st

def load_navbar_css():
    """Load CSS styles for navbar"""
    st.markdown("""
    <style>
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid var(--border);
        padding: 1rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 1px 6px var(--shadow);
    }

    .navbar-brand {
        font-family: 'Orbitron', monospace;
        font-size: 1.5rem;
        font-weight: 900;
        color: var(--matrix-green);
        text-decoration: none;
        text-shadow: 0 0 8px rgba(0, 255, 65, 0.3);
        letter-spacing: 1px;
        animation: matrix-glow 3s ease-in-out infinite;
    }

    @keyframes matrix-glow {
        0%, 100% { text-shadow: 0 0 8px rgba(0, 255, 65, 0.3); }
        50% { text-shadow: 0 0 16px rgba(0, 255, 65, 0.6), 0 0 24px rgba(0, 255, 65, 0.4); }
    }

    .navbar-nav {
        display: flex;
        list-style: none;
        margin: 0;
        padding: 0;
        gap: 0;
    }

    .nav-link {
        color: var(--text-secondary);
        text-decoration: none;
        font-weight: 400;
        transition: all 0.2s ease;
        padding: 0.75rem 1.25rem;
        border-radius: 8px;
        font-size: 0.9rem;
    }

    .nav-link:hover {
        color: var(--primary);
        background: rgba(26, 115, 232, 0.08);
    }

    .sticky-navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid #dadce0;
        padding: 15px 30px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }

    .navbar-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
    }

    .menu-items {
        display: flex;
        align-items: center;
        gap: 30px;
    }

    .menu-link {
        text-decoration: none;
        color: #5f6368;
        font-weight: 400;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        padding: 8px 16px;
        border-radius: 8px;
    }

    .menu-link:hover {
        color: #1f77b4;
        background: rgba(31, 119, 180, 0.1);
    }

    .menu-link.active {
        color: #1f77b4;
        background: rgba(31, 119, 180, 0.15);
        border-bottom: 2px solid #1f77b4;
    }

    .logo {
        font-family: 'Inter', 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
        font-weight: 700;
        font-size: 1.8rem;
        color: #1a73e8;
        letter-spacing: -0.02em;
        background: linear-gradient(135deg, #1a73e8 0%, #34a853 50%, #ea4335 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: none;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .logo:hover {
        transform: translateY(-1px);
        filter: brightness(1.1);
    }
    
    .chip-icon {
        width: 24px;
        height: 24px;
        position: relative;
        display: inline-block;
        background: linear-gradient(135deg, #1a73e8, #34a853);
        border-radius: 4px;
        box-shadow: 0 0 8px rgba(26, 115, 232, 0.4);
        animation: chip-pulse 3s ease-in-out infinite;
    }
    
    .chip-icon::before {
        content: '';
        position: absolute;
        top: 4px;
        left: 4px;
        right: 4px;
        bottom: 4px;
        background: #0f1419;
        border-radius: 2px;
        border: 1px solid #34a853;
    }
    
    .chip-icon::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 8px;
        height: 8px;
        background: linear-gradient(45deg, #ea4335, #fbbc04);
        border-radius: 1px;
        box-shadow: 
            -4px -4px 0 -3px #1a73e8,
            4px -4px 0 -3px #1a73e8,
            -4px 4px 0 -3px #1a73e8,
            4px 4px 0 -3px #1a73e8,
            0 -6px 0 -4px #34a853,
            0 6px 0 -4px #34a853,
            -6px 0 0 -4px #34a853,
            6px 0 0 -4px #34a853;
    }
    
    @keyframes chip-pulse {
        0%, 100% {
            box-shadow: 0 0 8px rgba(26, 115, 232, 0.4);
            transform: scale(1);
        }
        50% {
            box-shadow: 
                0 0 12px rgba(26, 115, 232, 0.6),
                0 0 20px rgba(52, 168, 83, 0.3);
            transform: scale(1.05);
        }
    }

    body {
        padding-top: 80px;
    }

    /* Language selector styles */
    .language-selector {
        position: fixed;
        top: 15px;
        right: 30px;
        z-index: 1000;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 8px;
    }

    .language-btn {
        background: transparent;
        border: none;
        padding: 8px 12px;
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.2s ease;
        font-size: 14px;
        margin: 0 2px;
    }

    .language-btn:hover {
        background: rgba(26, 115, 232, 0.1);
    }

    .language-btn.active {
        background: var(--primary);
        color: white;
    }

    .language-dropdown select {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border: 1px solid #dadce0;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 14px;
        color: #5f6368;
        cursor: pointer;
        transition: all 0.2s ease;
        outline: none;
    }

    .language-dropdown select:hover {
        border-color: #1a73e8;
        box-shadow: 0 2px 8px rgba(26, 115, 232, 0.2);
    }

    .language-dropdown select:focus {
        border-color: #1a73e8;
        box-shadow: 0 0 0 3px rgba(26, 115, 232, 0.1);
    }

    /* Move the selectbox to navbar position */
    div[data-testid="column"]:nth-child(4) > div > div > div[data-testid="stSelectbox"] {
        position: fixed !important;
        top: 25px !important;
        right: 30px !important;
        z-index: 1000 !important;
        width: auto !important;
        min-width: 120px !important;
    }

    div[data-testid="column"]:nth-child(4) > div > div > div[data-testid="stSelectbox"] > div > div {
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid #dadce0 !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
    }

    div[data-testid="column"]:nth-child(4) > div > div > div[data-testid="stSelectbox"] select {
        background: transparent !important;
        color: #5f6368 !important;
        font-size: 14px !important;
        padding: 8px 12px !important;
        border: none !important;
    }

    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            padding: 1rem;
        }

        .navbar-nav {
            margin-top: 1rem;
            flex-wrap: wrap;
            justify-content: center;
            gap: 0.25rem;
        }

        .language-selector {
            top: 10px;
            right: 10px;
        }
    }
    </style>
    """, unsafe_allow_html=True)