import streamlit as st

def load_components_css():
    """Load CSS styles for components"""
    st.markdown("""
    <style>
    .hero-section {
        background: var(--surface);
        color: var(--text-primary);
        padding: 8rem 2rem 6rem 2rem;
        text-align: center;
        margin-top: 0;
        border-bottom: 1px solid var(--border-light);
    }

    .hero-title {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        color: var(--text-primary);
        line-height: 1.1;
        letter-spacing: -0.025em;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        margin-bottom: 2.5rem;
        color: var(--text-secondary);
        font-weight: 400;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.6;
    }

    .section {
        padding: 5rem 2rem;
        margin: 0;
        background: var(--surface);
    }

    .section:nth-child(even) {
        background: var(--surface-alt);
    }

    .section-title {
        font-family: 'Inter', sans-serif;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 3rem;
        color: var(--text-primary);
        font-weight: 600;
        line-height: 1.2;
        letter-spacing: -0.025em;
    }

    .card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 2rem;
        box-shadow: var(--shadow);
        margin-bottom: 1.5rem;
        transition: all 0.15s ease;
    }

    .card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
        border-color: var(--primary);
    }

    .card h3 {
        color: var(--text-primary);
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1.25rem;
        margin-bottom: 1rem;
        line-height: 1.3;
    }

    .card p {
        color: var(--text-secondary);
        line-height: 1.6;
        font-size: 0.875rem;
        font-weight: 400;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
        max-width: 1000px;
        margin-left: auto;
        margin-right: auto;
    }

    .metric-card {
        background: var(--surface);
        color: var(--text-primary);
        padding: 2rem;
        border: 1px solid var(--border);
        border-radius: 8px;
        text-align: center;
        box-shadow: var(--shadow);
        transition: all 0.15s ease;
    }

    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
        border-color: var(--primary);
    }

    .metric-value {
        font-family: 'Inter', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: var(--primary);
    }

    .metric-label {
        font-size: 0.875rem;
        color: var(--text-secondary);
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
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