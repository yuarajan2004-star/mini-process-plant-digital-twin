import pandas as pd
import streamlit as st

from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Mini Process Plant DT",
    layout="wide"
)

st_autorefresh(
    interval=5000,
    key="refresh"
)

FILE = "../../08_Data/Historian/plant_historian.csv"

df = pd.read_csv(FILE)

latest = df.iloc[-1]

pressure = latest["PT101"]
flow = latest["FT101"]
temperature = latest["TT101"]
alarm = []

if pressure < 0.85:
    alarm.append("LOW PRESSURE")

if pressure > 1.15:
    alarm.append("HIGH PRESSURE")

if flow < 95:
    alarm.append("LOW FLOW")

if temperature > 33:
    alarm.append("HIGH TEMPERATURE")
pump = latest["Pump_Status"]
st.divider()

st.subheader("Alarm Panel")

if len(alarm) == 0:

    st.success(
        "NO ACTIVE ALARMS"
    )

else:

    for a in alarm:

        st.error(a)

health = 100

if pressure < 0.90:
    health -= 10

if flow < 100:
    health -= 10

if temperature > 32:
    health -= 10
st.subheader(
    "Equipment Health"
)

st.progress(
    health/100
)

st.metric(
    "Health Score (%)",
    health
)
st.title("Mini Process Plant Digital Twin")

c1,c2,c3,c4 = st.columns(4)

c1.metric("Pressure (bar)", pressure)
c2.metric("Flow (L/hr)", flow)
c3.metric("Temperature (°C)", temperature)
c4.metric("Pump Status",
          "RUNNING" if pump == 1 else "STOPPED")

st.divider()

st.subheader("Pressure Trend")
st.line_chart(df["PT101"])

st.subheader("Flow Trend")
st.line_chart(df["FT101"])

st.subheader("Temperature Trend")
st.line_chart(df["TT101"])
