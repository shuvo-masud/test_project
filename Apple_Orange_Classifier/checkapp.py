import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow import keras

# Load model
model = keras.models.load_model("fruit_classifier_v1.keras")

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

    if prediction > 0.9993:
        st.success("Prediction: 🍊 Orange")
        st.success(prediction)
    elif prediction >= 0.8 and prediction <= 0.9993:
        st.success("Prediction: Close to 🍊 Orange")
        st.success(prediction)
    elif prediction >= 0.2 and prediction < 0.8:
        st.success("Prediction: ❓ Unknown")
        st.success(prediction)
    elif prediction >= 0.0007 and prediction < 0.2:
        st.success("Prediction: Close to 🍎 Apple")
        st.success(prediction)

    else:
        st.success("Prediction: 🍎 Apple")
        st.success(prediction)