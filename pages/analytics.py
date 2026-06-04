import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Crop Analytics Dashboard")

# ---------------- DATA ----------------
data = {
    "Crop": ["Wheat", "Rice", "Maize", "Sugarcane", "Jute"],
    "Images": [180, 200, 170, 160, 150]
}

df = pd.DataFrame(data)

# ---------------- BAR CHART ----------------
st.subheader("📈 Crop Distribution")

fig = px.bar(
    df,
    x="Crop",
    y="Images",
    color="Crop",
    text="Images"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- PIE CHART ----------------
st.subheader("🥧 Dataset Share")

pie = px.pie(
    df,
    names="Crop",
    values="Images",
    hole=0.4
)

st.plotly_chart(pie, use_container_width=True)

# ---------------- LINE CHART ----------------
st.subheader("📉 Dataset Growth")

trend = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Images": [100, 200, 400, 650, 860]
})

line = px.line(
    trend,
    x="Month",
    y="Images",
    markers=True
)

st.plotly_chart(line, use_container_width=True)
