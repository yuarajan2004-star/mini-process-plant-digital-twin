import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Mini Process Plant DT",
    layout="wide"
)

st.title("Mini Process Plant Digital Twin")

FILE = "../../08_Data/Historian/plant_historian.csv"

df = pd.read_csv(FILE)

st.subheader("Latest Process Values")

latest = df.iloc[-1]

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Pressure (bar)",
    latest["PT101"]
)

c2.metric(
    "Flow (L/hr)",
    latest["FT101"]
)

c3.metric(
    "Temperature (°C)",
    latest["TT101"]
)

c4.metric(
    "Pump",
    "RUNNING" if latest["Pump_Status"]==1 else "STOPPED"
)

st.subheader("Pressure Trend")

st.line_chart(df["PT101"])

st.subheader("Flow Trend")

st.line_chart(df["FT101"])

st.subheader("Temperature Trend")

st.line_chart(df["TT101"])

st.subheader("Historian Data")

st.dataframe(df.tail(20))
