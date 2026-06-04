from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np

def preprocess_image(image):

    image = image.resize((224, 224))

    image = img_to_array(image)

    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    return image
