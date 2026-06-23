import pandas as pd
import streamlit as st
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
# DATA SOURCE
# =====================================================

FILE = "/home/yuarajan_s/Mini_Process_Plant_DT/08_Data/Historian/plant_historian.csv"

df = pd.read_csv(FILE)

latest = df.iloc[-1]

pressure = latest["PT101"]
flow = latest["FT101"]
temperature = latest["TT101"]
pump = latest["Pump_Status"]

# =====================================================
# ALARM ENGINE
# =====================================================

alarms = []

if pressure < 0.85:
    alarms.append("LOW PRESSURE")

if pressure > 1.15:
    alarms.append("HIGH PRESSURE")

if flow < 95:
    alarms.append("LOW FLOW")

if temperature > 33:
    alarms.append("HIGH TEMPERATURE")

# =====================================================
# EQUIPMENT HEALTH SCORE
# =====================================================

health = 100

# Warning thresholds (less aggressive)

if pressure < 0.85:
    health -= 10

if flow < 95:
    health -= 10

if temperature > 33:
    health -= 10

if len(alarms) > 0:
    health -= 10

health = max(0, health)

# =====================================================
# HEADER
# =====================================================

st.title("Mini Process Plant Digital Twin")

# =====================================================
# PLANT STATUS
# =====================================================

if len(alarms) == 0:

    st.success(
        "PLANT STATUS : NORMAL OPERATION"
    )

else:

    st.error(
        "PLANT STATUS : ALARM CONDITION"
    )

# =====================================================
# KPI SECTION
# =====================================================

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Pressure (bar)",
    round(float(pressure), 2)
)

c2.metric(
    "Flow (L/hr)",
    round(float(flow), 2)
)

c3.metric(
    "Temperature (°C)",
    round(float(temperature), 2)
)

c4.metric(
    "Pump",
    "RUNNING" if pump == 1 else "STOPPED"
)

# =====================================================
# ALARM PANEL
# =====================================================

st.divider()

st.subheader("Alarm Panel")

if len(alarms) == 0:

    st.success(
        "NO ACTIVE ALARMS"
    )

else:

    for alarm in alarms:

        st.error(alarm)

# =====================================================
# EQUIPMENT HEALTH
# =====================================================

st.divider()

st.subheader("Equipment Health")

st.progress(health / 100)

st.metric(
    "Health Score (%)",
    health
)

# =====================================================
# TRENDS
# =====================================================

st.divider()

st.subheader("Pressure Trend")

st.line_chart(df["PT101"])

st.subheader("Flow Trend")

st.line_chart(df["FT101"])

st.subheader("Temperature Trend")

st.line_chart(df["TT101"])

# =====================================================
# HISTORIAN
# =====================================================

st.divider()

st.subheader("Historian Data")

st.dataframe(
    df.tail(20),
    use_container_width=True
)
