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
pump = latest["Pump_Status"]

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
