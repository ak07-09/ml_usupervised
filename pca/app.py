import streamlit as st
from src.predict import run_inverse_inference

st.set_page_config(page_title="PCA Inverse Matrix", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    .stApp { background-color: #000000; font-family: 'Inter', sans-serif; color: #FFFFFF; }
    
    .hero-container { display: flex; align-items: center; justify-content: space-between; background: linear-gradient(135deg, #f97316 0%, #000000 100%); padding: 50px; border-radius: 12px; margin-bottom: 40px; border: 1px solid #ea580c; box-shadow: 0 10px 40px rgba(249, 115, 22, 0.1); }
    .hero-title { font-size: 4.5rem; font-weight: 900; letter-spacing: -2px; margin: 0; line-height: 1.1; color: #FFFFFF; }
    .hero-subtitle { font-size: 1.1rem; color: #fdba74; font-weight: 500; margin-top: 15px; }
    
    .stSlider label { font-size: 1.1rem !important; font-weight: 700 !important; color: #FFFFFF !important; margin-bottom: 5px; }
    div[data-testid="stThumbValue"] { font-size: 1rem !important; font-weight: 800 !important; color: #f97316 !important; }
    .stSlider > div > div > div > div { background-color: #f97316 !important; }
    
    .result-card { background-color: #0a0a0a; padding: 40px; border-radius: 8px; border: 1px solid #262626; }
    
    div[data-testid="stMetricValue"] { font-size: 2.5rem !important; font-weight: 900 !important; color: #f97316 !important; letter-spacing: -1px; }
    div[data-testid="stMetricLabel"] { color: #a3a3a3 !important; font-size: 0.9rem !important; font-weight: 700 !important; text-transform: uppercase; letter-spacing: 1px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero-container'>
    <div class='hero-left'>
        <h1 class='hero-title'>The Lifestyle Architect</h1>
        <p class='hero-subtitle'>PCA Inverse Matrix. Select the coordinate you want to reach on the mathematical plane. We generate the exact daily routine required to get there.</p>
    </div>
    <div class='hero-right'>
        <div style="font-size: 6rem;">🔄</div>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("<h3 style='font-weight: 900; margin-bottom: 20px;'>TARGET YOUR VIBE</h3>", unsafe_allow_html=True)
    pc1 = st.slider("Intensity Axis (PC1) - [Left = Chill, Right = Tryhard]", -4.0, 4.0, 0.0, 0.1)
    pc2 = st.slider("Chaos Axis (PC2) - [Left = Organized, Right = Goblin Mode]", -4.0, 4.0, 0.0, 0.1)

with col2:
    routine = run_inverse_inference(pc1, pc2)
    
    html_str = f"<div style='background: linear-gradient(180deg, #f97316 0%, #000000 100%); padding: 2px; border-radius: 10px;'><div class='result-card'><div style='color: #FFFFFF; font-weight: 800; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 30px;'>Required Daily Protocol</div></div></div>"
    st.markdown(html_str, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    r1, r2 = st.columns(2)
    r1.metric("Doomscrolling", f"{routine['doomscroll_hrs']:.1f} Hrs")
    r2.metric("Deep Focus", f"{routine['deep_focus_hrs']:.1f} Hrs")
    
    st.markdown("<br>", unsafe_allow_html=True)
    r3, r4 = st.columns(2)
    r3.metric("Caffeine Intake", f"{routine['caffeine_mg']:.0f} mg")
    r4.metric("Touching Grass", f"{routine['touch_grass_mins']:.0f} Mins")