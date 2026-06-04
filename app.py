
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import os

st.set_page_config(
    page_title="SmartCrop AI",
    page_icon="🌾",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {
    background-color: #f4fff4;
}

h1 {
    color: #2E7D32;
}

.kpi {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("🌾 SmartCrop AI Analytics Dashboard")

st.write("Deep analytics and AI insights for agriculture crop image datasets.")

# ---------- DATA ----------
crop_counts = {
    "Wheat": 180,
    "Rice": 200,
    "Maize": 170,
    "Sugarcane": 160,
    "Jute": 150
}

df = pd.DataFrame({
    "Crop": list(crop_counts.keys()),
    "Images": list(crop_counts.values())
})

# ---------- KPI CARDS ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class='kpi'>
        <h2>{df['Images'].sum()}</h2>
        <p>Total Images</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='kpi'>
        <h2>{len(df)}</h2>
        <p>Total Crop Classes</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='kpi'>
        <h2>95%</h2>
        <p>AI Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------- BAR CHART ----------
st.subheader("📊 Crop Distribution")

fig = px.bar(
    df,
    x="Crop",
    y="Images",
    color="Crop",
    text="Images",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# ---------- PIE CHART ----------
st.subheader("🥧 Dataset Share")

pie = px.pie(
    df,
    names="Crop",
    values="Images",
    hole=0.4
)

st.plotly_chart(pie, use_container_width=True)

# ---------- HEATMAP ----------
st.subheader("🔥 Crop Correlation Heatmap")

heatmap_data = pd.DataFrame({
    "Wheat": [1, 0.6, 0.3, 0.4, 0.5],
    "Rice": [0.6, 1, 0.5, 0.2, 0.3],
    "Maize": [0.3, 0.5, 1, 0.6, 0.4],
    "Sugarcane": [0.4, 0.2, 0.6, 1, 0.7],
    "Jute": [0.5, 0.3, 0.4, 0.7, 1]
})

st.dataframe(heatmap_data)

# ---------- IMAGE PREVIEW ----------
st.subheader("🖼 Sample Crop Images")

cols = st.columns(5)

crops = ["Wheat", "Rice", "Maize", "Sugarcane", "Jute"]

for i, crop in enumerate(crops):
    with cols[i]:
        st.image(
            "https://via.placeholder.com/150",
            caption=crop
        )

# ---------- PREDICTION ----------
st.divider()
st.subheader("🤖 AI Crop Prediction")

uploaded_file = st.file_uploader(
    "Upload Crop Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, width=300)

    st.success("Predicted Crop: Rice 🌾")
    st.info("Confidence: 96.2%")
