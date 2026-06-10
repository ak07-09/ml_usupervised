import streamlit as st
from src.predict import run_inference

st.set_page_config(page_title="Identity Mixture Model", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&display=swap');
    
    .stApp { background-color: #09090b; font-family: 'Outfit', sans-serif; color: #FFFFFF; }
    
    .hero-container { display: flex; align-items: center; justify-content: space-between; background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%); padding: 50px; border-radius: 12px; margin-bottom: 40px; box-shadow: 0 10px 40px rgba(236, 72, 153, 0.15); }
    .hero-title { font-size: 4.5rem; font-weight: 900; letter-spacing: -2px; margin: 0; line-height: 1.1; color: #FFFFFF; }
    .hero-subtitle { font-size: 1.1rem; color: #fdf2f8; font-weight: 500; margin-top: 15px; }
    
    .stSlider label { font-size: 1.1rem !important; font-weight: 700 !important; color: #FFFFFF !important; margin-bottom: 5px; }
    div[data-testid="stThumbValue"] { font-size: 1rem !important; font-weight: 800 !important; color: #ec4899 !important; }
    .stSlider > div > div > div > div { background-color: #ec4899 !important; }
    
    .stButton > button { background: linear-gradient(90deg, #a855f7 0%, #ec4899 100%) !important; color: #FFFFFF !important; border-radius: 8px !important; font-weight: 800 !important; padding: 20px !important; width: 100%; border: none !important; letter-spacing: 2px; text-transform: uppercase; margin-top: 25px; transition: transform 0.2s ease; }
    .stButton > button:hover { transform: scale(1.02); }
    
    .result-card { background-color: #18181b; padding: 40px; border-radius: 8px; border: 1px solid #27272a; }
    .prob-bar-container { background-color: #27272a; border-radius: 6px; height: 16px; margin-top: 8px; margin-bottom: 25px; overflow: hidden; }
    .prob-bar { height: 100%; border-radius: 6px; transition: width 0.5s ease-in-out; }
    .stat-label { font-weight: 700; font-size: 0.95rem; text-transform: uppercase; color: #e4e4e7; display: flex; justify-content: space-between; letter-spacing: 0.5px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero-container'>
    <div class='hero-left'>
        <h1 class='hero-title'>Gaussian Identity Matrix</h1>
        <p class='hero-subtitle'>GMM doesn't put you in one box. It calculates the exact soft-clustering probability of your aesthetic overlap.</p>
    </div>
    <div class='hero-right'>
        <div style="font-size: 6rem; text-shadow: 0 0 30px rgba(255,255,255,0.3);">🎭</div>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    rizz = st.slider("Rizz (Charisma)", 0, 10, 5)
    aura = st.slider("Aura (Presence)", 0, 10, 6)
    lore = st.slider("Lore (Backstory/Trauma)", 0, 10, 3)
    delusion = st.slider("Delusion", 0, 10, 8)
    scan_btn = st.button("CALCULATE PROBABILITIES")

with col2:
    if scan_btn:
        probs, cluster = run_inference({
            'rizz': rizz, 'aura': aura, 
            'lore': lore, 'delusion': delusion
        })
        
        c1_p, c2_p, c3_p = probs[0]*100, probs[1]*100, probs[2]*100
        
        # SLEDGEHAMMER FIX: The entire HTML string is now forced onto ONE single line. 
        # Streamlit cannot indent this or treat it as a code block.
        html_str = f"<div class='result-card'><h2 style='margin-top: 0; font-weight: 900; font-size: 2.2rem; margin-bottom: 35px; letter-spacing: -1px;'>GMM Cluster Overlap</h2><div class='stat-label'><span>The Main Character (High Aura/Delusion)</span><span style='color: #ec4899;'>{c1_p:.1f}%</span></div><div class='prob-bar-container'><div class='prob-bar' style='width: {c1_p:.1f}%; background: linear-gradient(90deg, #be185d 0%, #ec4899 100%);'></div></div><div class='stat-label'><span>The Mysterious Local (High Lore)</span><span style='color: #a855f7;'>{c2_p:.1f}%</span></div><div class='prob-bar-container'><div class='prob-bar' style='width: {c2_p:.1f}%; background: linear-gradient(90deg, #7e22ce 0%, #a855f7 100%);'></div></div><div class='stat-label'><span>The NPC (Balanced)</span><span style='color: #06b6d4;'>{c3_p:.1f}%</span></div><div class='prob-bar-container'><div class='prob-bar' style='width: {c3_p:.1f}%; background: linear-gradient(90deg, #0369a1 0%, #06b6d4 100%);'></div></div></div>"
        
        st.markdown(html_str, unsafe_allow_html=True)