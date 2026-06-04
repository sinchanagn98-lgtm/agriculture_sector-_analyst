import streamlit as st
from PIL import Image

from utils.prediction import predict_crop

st.title("🤖 Crop Prediction")

uploaded_file = st.file_uploader(
    "Upload Crop Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, width=300)

    crop, confidence = predict_crop(image)

    st.success(f"Predicted Crop: {crop}")

    st.info(f"Confidence: {confidence*100:.2f}%")
