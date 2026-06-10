import streamlit as st
from src.predict import run_inverse_inference

st.set_page_config(page_title="t-SNE Aesthetic Synthesizer", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&display=swap');
    
    .stApp { background-color: #020617; font-family: 'Syne', sans-serif; color: #FFFFFF; }
    
    .hero-container { display: flex; align-items: center; justify-content: space-between; background: linear-gradient(135deg, #a3e635 0%, #020617 100%); padding: 50px; border-radius: 12px; margin-bottom: 40px; border: 1px solid #65a30d; box-shadow: 0 10px 40px rgba(163, 230, 53, 0.1); }
    .hero-title { font-size: 4.5rem; font-weight: 800; letter-spacing: -2px; margin: 0; line-height: 1.1; color: #FFFFFF; }
    .hero-subtitle { font-size: 1.1rem; color: #d9f99d; font-weight: 700; margin-top: 15px; }
    
    .stSlider label { font-size: 1.1rem !important; font-weight: 700 !important; color: #FFFFFF !important; margin-bottom: 5px; }
    div[data-testid="stThumbValue"] { font-size: 1rem !important; font-weight: 800 !important; color: #a3e635 !important; }
    .stSlider > div > div > div > div { background-color: #a3e635 !important; }
    
    .result-card { background-color: #0f172a; padding: 40px; border-radius: 8px; border: 1px solid #1e293b; }
    
    div[data-testid="stMetricValue"] { font-size: 2.5rem !important; font-weight: 800 !important; color: #a3e635 !important; letter-spacing: -1px; }
    div[data-testid="stMetricLabel"] { color: #94a3b8 !important; font-size: 0.9rem !important; font-weight: 700 !important; text-transform: uppercase; letter-spacing: 1px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero-container'>
    <div class='hero-left'>
        <h1 class='hero-title'>The Aesthetic Synthesizer</h1>
        <p class='hero-subtitle'>t-SNE Part 2. Select a coordinate on the topological manifold. The generative KNN bridge will reverse-engineer the exact fashion composition required to hit that aesthetic.</p>
    </div>
    <div class='hero-right'>
        <div style="font-size: 6rem;">🧬</div>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("<h3 style='font-weight: 800; margin-bottom: 20px;'>NAVIGATE THE MANIFOLD</h3>", unsafe_allow_html=True)
    tsne_x = st.slider("Manifold Dimension X", -50.0, 50.0, 0.0, 0.5)
    tsne_y = st.slider("Manifold Dimension Y", -50.0, 50.0, 0.0, 0.5)

with col2:
    stats = run_inverse_inference(tsne_x, tsne_y)
    
    html_str = f"<div style='background: linear-gradient(180deg, #a3e635 0%, #020617 100%); padding: 2px; border-radius: 10px;'><div class='result-card'><div style='color: #FFFFFF; font-weight: 800; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 30px;'>Target Aesthetic Composition</div></div></div>"
    st.markdown(html_str, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    r1, r2 = st.columns(2)
    r1.metric("Thrift / Vintage Energy", f"{stats['thrift_energy']:.0f}%")
    r2.metric("Gorpcore / Utility", f"{stats['gorpcore_utility' ]:.0f}%")
    
    st.markdown("<br>", unsafe_allow_html=True)
    r3, r4 = st.columns(2)
    r3.metric("Y2K Nostalgia", f"{stats['y2k_nostalgia']:.0f}%")
    r4.metric("Avant-Garde", f"{stats['avant_garde']:.0f}%")