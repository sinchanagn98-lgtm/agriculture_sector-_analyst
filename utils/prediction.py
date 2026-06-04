import tensorflow as tf
import numpy as np

from utils.preprocessing import preprocess_image

# ---------------- LOAD MODEL ----------------
model = tf.keras.models.load_model(
    "models/crop_classifier.h5"
)

# ---------------- CLASS LABELS ----------------
classes = [
    "Wheat",
    "Rice",
    "Maize",
    "Sugarcane",
    "Jute"
]

# ---------------- PREDICTION FUNCTION ----------------
def predict_crop(image):

    processed = preprocess_image(image)

    prediction = model.predict(processed)

    index = np.argmax(prediction)

    confidence = prediction[0][index]

    return classes[index], confidence
