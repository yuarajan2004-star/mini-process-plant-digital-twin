import pandas as pd
import streamlit as st
import joblib

from streamlit_autorefresh import st_autorefresh

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Mini Process Plant Digital Twin",
    layout="wide"
)

# =====================================================
# AUTO REFRESH
# =====================================================

st_autorefresh(
    interval=5000,
    key="refresh"
)

# =====================================================
# FILES
# =====================================================

DATA_FILE = "/home/yuarajan_s/Mini_Process_Plant_DT/08_Data/Historian/plant_historian.csv"

MODEL_FILE = "/home/yuarajan_s/Mini_Process_Plant_DT/09_AI_Model/Models/fault_classifier.pkl"

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv(DATA_FILE)

latest = df.iloc[-1]

pressure = latest["PT101"]
flow = latest["FT101"]
temperature = latest["TT101"]
pump = latest["Pump_Status"]

# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load(MODEL_FILE)

prediction_input = pd.DataFrame(
    [[pressure, flow, temperature]],
    columns=[
        "PT101",
        "FT101",
        "TT101"
    ]
)

prediction = model.predict(
    prediction_input
)[0]

fault_map = {

    0: "NORMAL",

    1: "LOW PRESSURE",

    2: "HIGH PRESSURE",

    3: "LOW FLOW",

    4: "HIGH TEMPERATURE",

    5: "COMBINED FAULT"
}

fault_text = fault_map[prediction]

# =====================================================
# HEALTH SCORE
# =====================================================

health = 100

if prediction != 0:
    health -= 20

health = max(0, health)

# =====================================================
# TITLE
# =====================================================

st.title(
    "Mini Process Plant Digital Twin"
)

# =====================================================
# AI STATUS
# =====================================================

st.subheader(
    "AI Predictive Maintenance"
)

if prediction == 0:

    st.success(
        f"AI Prediction : {fault_text}"
    )

else:

    st.error(
        f"AI Prediction : {fault_text}"
    )

# =====================================================
# HEALTH
# =====================================================

st.subheader(
    "Equipment Health"
)

st.progress(
    health / 100
)

st.metric(
    "Health Score (%)",
    health
)

# =====================================================
# KPI SECTION
# =====================================================

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Pressure (bar)",
    round(float(pressure),2)
)

c2.metric(
    "Flow (L/hr)",
    round(float(flow),2)
)

c3.metric(
    "Temperature (°C)",
    round(float(temperature),2)
)

c4.metric(
    "Pump",
    "RUNNING" if pump == 1 else "STOPPED"
)

# =====================================================
# RECOMMENDATION
# =====================================================

st.subheader(
    "Maintenance Recommendation"
)

recommendation = {

    "NORMAL":
        "No action required",

    "LOW PRESSURE":
        "Inspect pump suction and leakage",

    "HIGH PRESSURE":
        "Inspect downstream blockage",

    "LOW FLOW":
        "Check valve restriction and pump condition",

    "HIGH TEMPERATURE":
        "Inspect cooling and operating conditions",

    "COMBINED FAULT":
        "Immediate maintenance inspection required"
}

st.info(
    recommendation[fault_text]
)

# =====================================================
# TRENDS
# =====================================================

st.subheader(
    "Pressure Trend"
)

st.line_chart(
    df["PT101"]
)

st.subheader(
    "Flow Trend"
)

st.line_chart(
    df["FT101"]
)

st.subheader(
    "Temperature Trend"
)

st.line_chart(
    df["TT101"]
)

# =====================================================
# HISTORIAN
# =====================================================

st.subheader(
    "Historian Data"
)

st.dataframe(
    df.tail(20),
    use_container_width=True
)
