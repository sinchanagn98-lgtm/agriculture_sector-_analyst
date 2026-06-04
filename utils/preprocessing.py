import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model(
    "models/crop_classifier.h5"
)

classes = [
    "Wheat",
    "Rice",
    "Maize",
    "Sugarcane",
    "Jute"
]

def predict_crop(image):

    image = image.resize((224, 224))

    img = np.array(image) / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    index = np.argmax(prediction)

    return classes[index], prediction[0][index]
