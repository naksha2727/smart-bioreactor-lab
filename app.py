import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from reactor_model import simulate_growth
from ui_components import show_info

st.set_page_config(page_title="Smart Bioreactor Lab", layout="wide")

# Custom CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🧪 Smart Bioreactor Control Virtual Lab")

# Tabs like professional lab UI
tab1, tab2, tab3 = st.tabs(["🧫 Simulation", "📊 Results", "📘 Theory"])

# ---------------- TAB 1 ----------------
with tab1:
    st.header("Control Panel")

    col1, col2 = st.columns(2)

    with col1:
        temp = st.slider("Temperature (°C)", 20, 50, 37)
        pH = st.slider("pH Level", 4.0, 9.0, 7.0)

    with col2:
        oxygen = st.slider("Oxygen Level (%)", 0, 100, 50)
        stir = st.slider("Stirring Speed (rpm)", 50, 500, 200)

    start = st.button("▶ Run Simulation")

    if start:
        time, biomass = simulate_growth(temp, pH, oxygen, stir)
        st.session_state["time"] = time
        st.session_state["biomass"] = biomass
        st.success("Simulation Completed!")

# ---------------- TAB 2 ----------------
with tab2:
    st.header("Growth Curve")

    if "time" in st.session_state:
        fig, ax = plt.subplots()
        ax.plot(st.session_state["time"], st.session_state["biomass"])
        ax.set_xlabel("Time")
        ax.set_ylabel("Biomass")
        ax.set_title("Bioreactor Growth Curve")
        st.pyplot(fig)

        st.metric("Final Biomass", f"{st.session_state['biomass'][-1]:.2f}")
    else:
        st.warning("Run simulation first!")

# ---------------- TAB 3 ----------------
with tab3:
    show_info()
