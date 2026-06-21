
import streamlit as st
import math

st.title("Flooded Tubular Lead-Acid Battery Life Predictor")

st.markdown("Estimate SOH and Remaining Useful Life (RUL) from EIS and aging data.")

st.header("Input Measurements")

capacity_now = st.number_input("Current Capacity (Ah)", value=140.0)
capacity_initial = st.number_input("Initial Capacity (Ah)", value=150.0)

rct_now = st.number_input("Current Rct (mΩ)", value=4.0)
rct_initial = st.number_input("Initial Rct (mΩ)", value=2.0)
rct_critical = st.number_input("Critical Rct at EOL (mΩ)", value=10.0)
rct_growth = st.number_input("Observed dRct/dt (mΩ/week)", value=0.05)

rs_now = st.number_input("Current Rs (mΩ)", value=1.2)
rs_initial = st.number_input("Initial Rs (mΩ)", value=1.0)

cpe_now = st.number_input("Current CPE value", value=0.85)
cpe_initial = st.number_input("Initial CPE value", value=1.0)

water_loss = st.number_input("Water Loss (% of initial inventory)", value=10.0)

st.header("Model Weights")
w1 = st.slider("Rct Weight", 0.0, 1.0, 0.5)
w2 = st.slider("CPE Weight", 0.0, 1.0, 0.3)
w3 = st.slider("Rs Weight", 0.0, 1.0, 0.2)

weight_sum = max(w1+w2+w3, 1e-9)

capacity_ratio = capacity_now / capacity_initial
health_index = (
    w1*(rct_initial/max(rct_now,1e-9)) +
    w2*(cpe_now/max(cpe_initial,1e-9)) +
    w3*(rs_initial/max(rs_now,1e-9))
)/weight_sum

soh = 100*(0.5*capacity_ratio + 0.5*health_index)

rul_weeks = (rct_critical - rct_now)/max(rct_growth,1e-9)
rul_weeks = max(0, rul_weeks)

st.header("Results")
st.metric("Estimated SOH (%)", round(soh,1))
st.metric("Health Index", round(health_index,3))
st.metric("Estimated RUL (weeks)", round(rul_weeks,1))
st.metric("Estimated RUL (years)", round(rul_weeks/52,2))

st.info("Model is a first-order engineering estimator and must be calibrated using endurance and accelerated life data.")
