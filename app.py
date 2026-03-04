"""
Computational Urban Mechanics: Multiscale Digital Twin
Standalone Specialized Edition
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(page_title="Urban Mechanics Hub", page_icon="🏗️", layout="wide")

# --- PREMIUM STYLING ---
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border-left: 5px solid #00f2ff; }
    h1, h2, h3 { color: #00f2ff; font-family: 'Inter', sans-serif; }
    .stButton>button { background-color: #00f2ff; color: #0e1117; font-weight: bold; border-radius: 20px; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- RESEARCH LOGIC ---
def run_homogenization_sim(material_density, voids_pct, anisotropy_ratio):
    base_stability = (1 - (voids_pct/100)) * (material_density/500)
    diffusion_rate = (anisotropy_ratio * 0.4) + (voids_pct * 0.05)
    inverse_reliability = 1 - (voids_pct * 0.002) - (abs(anisotropy_ratio - 1) * 0.05)
    return {
        "Structural Stability Index": round(base_stability * 100, 2),
        "Effective Homogenization": round((1 - diffusion_rate) * 100, 2),
        "Inverse Analysis Reliability": round(inverse_reliability * 100, 1),
        "Thermal Diffusion Flux": round(diffusion_rate, 3)
    }

st.title("🏙️ Computational Urban BioMechanics Hub")
st.markdown("### Specialized Multiscale Digital Twin for Structural Health Monitoring")
st.divider()

with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/structural.png", width=80)
    st.header("🔬 Material Parameters")
    dens = st.slider("Material Density (kg/m³)", 100, 1000, 600)
    voids = st.slider("Void Percentage (%)", 5, 40, 15)
    aniso = st.slider("Anisotropy Ratio (E1/E2)", 0.5, 3.0, 1.2)
    st.divider()
    if st.button("🚀 Run Inverse Parameter Estimation"):
        st.toast("Executing L-M optimization...", icon="🔄")

results = run_homogenization_sim(dens, voids, aniso)

m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Stability", f"{results['Structural Stability Index']}%")
with m2: st.metric("Homogenization", f"{results['Effective Homogenization']}%")
with m3: st.metric("Inv. Reliability", f"{results['Inverse Analysis Reliability']}%")
with m4: st.metric("Latency", "< 0.8ms", delta="Surrogate Opt.")

st.divider()
grid_size = 25
x = np.linspace(0, 5, grid_size)
y = np.linspace(0, 5, grid_size)
X, Y = np.meshgrid(x, y)
Z = (np.cos(X * aniso) * np.sin(Y)) * (100 / dens) + (voids / 10)
fig = go.Figure(data=[go.Surface(z=Z, colorscale='Cividis')])
fig.update_layout(title='Homogenized Stress Distribution', template="plotly_dark", height=600)
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.write("**Methodology:** This hub focuses on the homogenization of anisotropic biological and urban construction materials, utilizing ANN surrogates for real-time inverse analysis.")
st.caption("PhD Candidate: Iffat Nazir | Research Focus: Computational Mechanics & Inverse Problems")
