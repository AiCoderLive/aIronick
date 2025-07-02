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
        z-index: 1001;
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
        z-index: 1001;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid var(--border-light);
        padding: 1rem 2rem;
        box-shadow: var(--shadow);
    }

    .aironick-navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 9999;
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(15px);
        border-bottom: 1px solid #e0e0e0;
        padding: 12px 0;
        box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    .navbar-container {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 30px;
    }
    
    .navbar-logo {
        font-size: 24px;
        font-weight: 800;
        background: linear-gradient(135deg, #1a73e8 0%, #34a853 50%, #ea4335 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 8px;
        cursor: pointer;
    }
    
    .navbar-menu {
        display: flex;
        align-items: center;
        gap: 0;
        list-style: none;
        margin: 0;
        padding: 0;
    }
    
    .navbar-link {
        display: inline-block;
        padding: 12px 20px;
        text-decoration: none;
        color: #5f6368;
        font-weight: 500;
        font-size: 16px;
        transition: all 0.3s ease;
        border-radius: 8px;
        position: relative;
        cursor: pointer;
    }
    
    .navbar-link:hover {
        color: #1a73e8;
        background: rgba(26, 115, 232, 0.08);
        transform: translateY(-1px);
    }
    
    .navbar-link:active {
        transform: translateY(0);
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
        text-decoration: none !important;
        color: var(--text-secondary);
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        font-size: 0.875rem;
        transition: all 0.15s ease;
        padding: 0.75rem 1.25rem;
        border-radius: 6px;
        display: inline-block;
        background: transparent;
        border: 1px solid transparent;
        cursor: pointer;
        position: relative;
        white-space: nowrap;
        user-select: none;
    }

    .menu-link:link,
    .menu-link:visited,
    .menu-link:hover,
    .menu-link:active {
        text-decoration: none !important;
        outline: none;
    }

    .menu-link:hover {
        color: var(--primary);
        background: rgb(37 99 235 / 0.1);
        border-color: rgb(37 99 235 / 0.2);
        transform: translateY(-1px);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .menu-link.active {
        color: var(--primary);
        background: rgb(37 99 235 / 0.15);
        border-color: rgb(37 99 235 / 0.3);
        font-weight: 600;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .menu-link:focus {
        outline: 2px solid var(--primary);
        outline-offset: 2px;
    }

    .logo {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 1.5rem;
        color: var(--text-primary);
        letter-spacing: -0.02em;
        transition: all 0.15s ease;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .logo:hover {
        color: var(--primary);
    }
    
    .chip-icon {
        width: 20px;
        height: 20px;
        position: relative;
        display: inline-block;
        background: var(--primary);
        border-radius: 4px;
        box-shadow: var(--shadow);
    }
    
    .chip-icon::before {
        content: '';
        position: absolute;
        top: 3px;
        left: 3px;
        right: 3px;
        bottom: 3px;
        background: var(--surface);
        border-radius: 2px;
        border: 1px solid var(--primary);
    }
    
    .chip-icon::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 6px;
        height: 6px;
        background: var(--primary);
        border-radius: 1px;
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

    /* Mobile optimizations */
    @media (max-width: 768px) {
        .sticky-navbar {
            padding: 0.75rem 1rem;
        }
        
        .menu-items {
            gap: 1rem;
            flex-wrap: wrap;
        }
        
        .menu-link {
            padding: 1rem 1.5rem;
            font-size: 0.875rem;
            min-height: 48px; /* Touch target size */
            min-width: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        
        .logo {
            font-size: 1.25rem;
        }
        
        .chip-icon {
            width: 18px;
            height: 18px;
        }
    }
    
    /* Touch device optimizations */
    @media (hover: none) and (pointer: coarse) {
        .menu-link {
            min-height: 48px;
            padding: 1rem 1.25rem;
        }
        
        .menu-link:hover {
            transform: none;
            background: rgb(37 99 235 / 0.15);
        }
    }
    </style>
    """, unsafe_allow_html=True)