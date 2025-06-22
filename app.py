import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(
    page_title="aIRONick",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&display=swap');
    
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
    }
    </style>
    """, unsafe_allow_html=True)

def create_navbar():
    st.markdown("""
    <div class="navbar">
        <div class="navbar-brand">🤖 aIRONick</div>
        <nav class="navbar-nav">
            <a href="#home" class="nav-link">Home</a>
            <a href="#features" class="nav-link">Software testing</a>
            <a href="#analytics" class="nav-link">Electrician</a>
            <a href="#about" class="nav-link">Youtube</a>
            <a href="#contact" class="nav-link">Contact</a>
        </nav>
    </div>
    """, unsafe_allow_html=True)

def create_hero_section():
    st.markdown("""
    <div class="hero-section" id="home">
        <h1 class="hero-title">Professional Testing & Gaming Solutions</h1>
        <p class="hero-subtitle">aIRONick delivers comprehensive software testing, hardware testing, electrical services, and gaming solutions. From automation testing to console gaming setups, we've got you covered.</p>
        <a href="#features" class="cta-button">Our Services</a>
    </div>
    """, unsafe_allow_html=True)

def create_features_section():
    st.markdown("""
    <div class="section" id="features">
        <h2 class="section-title">Software testing</h2>
        <div class="feature-grid">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>🔧 Software Testing</h3>
            <p>Comprehensive automation testing, performance testing, and quality assurance services. We ensure your applications run flawlessly across all platforms and environments.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>🎮 Gaming Solutions</h3>
            <p>Professional gaming setups, console installations, gaming PC builds, and performance optimization for both competitive and casual gaming experiences.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>⚡ Hardware Testing</h3>
            <p>Professional hardware diagnostics, component testing, and system validation. From servers to consumer electronics, we ensure optimal performance and reliability.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>🔌 Electrical Services</h3>
            <p>Licensed electrical work including installations, repairs, wiring, and electrical system diagnostics. Safety-certified and code-compliant electrical solutions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

def create_analytics_section():
    st.markdown("""
    <div class="section" id="analytics">
        <h2 class="section-title">Electrician</h2>
        <div class="feature-grid">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>⚡ Residential Electrical</h3>
            <p>Complete home electrical services including wiring, outlet installation, panel upgrades, ceiling fans, lighting fixtures, and electrical repairs. Licensed and insured for your safety.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>🏢 Commercial Electrical</h3>
            <p>Professional commercial electrical work for businesses, offices, and industrial facilities. Emergency electrical services, maintenance contracts, and code compliance inspections.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>🔧 Electrical Troubleshooting</h3>
            <p>Expert diagnosis and repair of electrical problems. Circuit breaker issues, power outages, faulty wiring detection, and electrical safety inspections using advanced testing equipment.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>🔌 Smart Home Installation</h3>
            <p>Modern smart home electrical solutions including smart switches, outlets, home automation systems, EV charging stations, and energy-efficient LED lighting installations.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

def create_about_section():
    st.markdown("""
    <div class="section" id="about">
        <h2 class="section-title">YouTube</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎥 Watch Our Latest Videos")
    st.write("Check out our YouTube channel for tutorials, behind-the-scenes content, and tech insights. Subscribe to stay updated with our latest content!")
    
    # Create centered button using Streamlit
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Visit Our YouTube Channel", key="youtube_btn"):
            st.markdown('<meta http-equiv="refresh" content="0; url=https://www.youtube.com/@aIrOnick">', unsafe_allow_html=True)
        st.markdown("""
        <style>
        .stButton > button {
            background: linear-gradient(45deg, #ff0000, #cc0000);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 25px;
            font-weight: bold;
            font-size: 16px;
            width: 100%;
        }
        .stButton > button:hover {
            transform: scale(1.05);
            transition: transform 0.3s ease;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Featured playlists section
    st.markdown("### 📺 Featured Playlists")
    
    # Create playlist cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card" style="text-align: center;">
            <h4>🔧 Software Testing</h4>
            <p>Comprehensive tutorials on automated testing, performance testing, and QA best practices</p>
            <a href="https://www.youtube.com/@aIrOnick/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ Watch Playlist</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card" style="text-align: center;">
            <h4>🎮 Gaming Tech</h4>
            <p>Gaming setups, hardware reviews, and performance optimization guides</p>
            <a href="https://www.youtube.com/@aIrOnick/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ Watch Playlist</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card" style="text-align: center;">
            <h4>⚡ Electrical Work</h4>
            <p>Safety demonstrations, installation guides, and troubleshooting tips</p>
            <a href="https://www.youtube.com/@aIrOnick/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ Watch Playlist</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card" style="text-align: center;">
            <h4>💻 Hardware Reviews</h4>
            <p>In-depth hardware testing, diagnostics, and component reviews</p>
            <a href="https://www.youtube.com/@aIrOnick/playlists" target="_blank" style="color: #ff0000; text-decoration: none;">▶️ Watch Playlist</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def create_contact_section():
    st.markdown("""
    <div class="section" id="contact">
        <h2 class="section-title">Ready to get started?</h2>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Get in Touch</h3>
            <p>📧 Email: services@aironick.com</p>
            <p>📱 Phone: +1 (555) TEST-123</p>
            <p>🌐 Website: www.aironick.com</p>
            <p>📍 Service Area: Greater Metro Area</p>
            <p>⏰ Hours: Mon-Fri 9AM-6PM, Emergency services available</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Send us a message")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Email Address")
            service = st.selectbox("Service Needed", ["Software Testing", "Hardware Testing", "Electrical Services", "Gaming Solutions", "Multiple Services", "Consultation"])
            message = st.text_area("Project Details", height=100, placeholder="Describe your project requirements...")
            
            if st.form_submit_button("Request Quote"):
                if name and email and message:
                    st.success("Thank you! We'll provide a detailed quote within 24 hours.")
                else:
                    st.error("Please fill in all fields.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def create_footer():
    st.markdown("""
    <div class="footer">
        <p>&copy; 2024 aIRONick Technical Services. Licensed & Insured.</p>
        <p>Software Testing • Hardware Testing • Electrical Services • Gaming Solutions</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    load_custom_css()
    create_navbar()
    create_hero_section()
    create_features_section()
    create_analytics_section()
    create_about_section()
    create_contact_section()
    create_footer()

if __name__ == "__main__":
    main()