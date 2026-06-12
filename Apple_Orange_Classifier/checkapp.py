import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow import keras

# Load model
model = keras.models.load_model("apple_orange_model.keras")

img_size = (128, 128)

def prepare_image(img):
    img = keras.utils.img_to_array(img) / 255.0
    img = tf.image.resize(img, img_size)
    img = np.expand_dims(img, axis=0)
    return img

# UI
st.title("🍎 Apple vs 🍊 Orange Classifier")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    image = keras.utils.load_img(uploaded_file)
    processed = prepare_image(image)

    prediction = model.predict(processed)[0][0]

    if prediction > 0.5:
        st.success("Prediction: 🍊 Orange")
    else:
        st.success("Prediction: 🍎 Apple")