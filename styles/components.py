import streamlit as st

def load_components_css():
    """Load CSS styles for components"""
    st.markdown("""
    <style>
    .hero-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        color: var(--text-primary);
        padding: 8rem 2rem 5rem 2rem;
        text-align: center;
        margin-top: 0;
    }

    .hero-title {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        color: var(--text-primary);
        line-height: 1.1;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        margin-bottom: 2rem;
        color: var(--text-secondary);
        font-weight: 400;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.5;
    }

    .section {
        padding: 5rem 2rem;
        margin: 0;
        background: var(--surface);
    }

    .section:nth-child(even) {
        background: var(--background);
    }

    .section-title {
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 3rem;
        color: var(--text-primary);
        font-weight: 600;
        line-height: 1.2;
    }

    .card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 2px 8px var(--shadow);
        margin-bottom: 1.5rem;
        transition: all 0.2s ease;
    }

    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px var(--shadow-hover);
        border-color: var(--border-hover);
    }

    .card h3 {
        color: var(--text-primary);
        font-weight: 600;
        font-size: 1.25rem;
        margin-bottom: 1rem;
        line-height: 1.3;
    }

    .card p {
        color: var(--text-secondary);
        line-height: 1.6;
        font-size: 0.95rem;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }

    .metric-card {
        background: var(--surface);
        color: var(--text-primary);
        padding: 2rem;
        border: 1px solid var(--border);
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 2px 8px var(--shadow);
        transition: all 0.2s ease;
    }

    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px var(--shadow-hover);
    }

    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: var(--primary);
    }

    .metric-label {
        font-size: 0.9rem;
        color: var(--text-secondary);
        font-weight: 500;
    }

    .footer {
        background: var(--surface);
        color: var(--text-secondary);
        padding: 3rem 2rem;
        text-align: center;
        border-top: 1px solid var(--border);
        font-size: 0.9rem;
    }

    .cta-button {
        display: inline-block;
        background: var(--primary);
        color: white;
        padding: 1rem 2rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.2s ease;
        margin-top: 1rem;
    }

    .cta-button:hover {
        background: var(--primary-hover);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(26, 115, 232, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)