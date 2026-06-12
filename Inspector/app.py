import streamlit as st
import tensorflow as tf
import numpy as np
import joblib
from PIL import Image

# ==========================
# LOAD MODELS
# ==========================

fruit_model = tf.keras.models.load_model(
    "../Apple_Orange_Classifier/apple_orange_model.keras"
)

quality_model = joblib.load(
    "../Apple_Quality_Classifier/apple_quality_model.pkl"
)

IMG_SIZE = (128, 128)

st.title("🍎 Fruit Inspector (CNN + ML Hybrid)")

st.write("Upload an image to predict fruit type and quality.")

# ==========================
# FEATURE EXTRACTOR (CNN)
# ==========================

feature_extractor = tf.keras.Model(
    inputs=fruit_model.input,
    outputs=fruit_model.layers[-2].output  # second last layer = features
)

# ==========================
# IMAGE UPLOAD
# ==========================

uploaded_file = st.file_uploader(
    "Upload Fruit Image",
    type=["jpg", "jpeg", "png"]
)

# ==========================
# PREDICTION
# ==========================

if st.button("Predict"):

    if uploaded_file is None:
        st.error("Please upload an image.")
        st.stop()

    # ==========================
    # IMAGE PROCESSING
    # ==========================

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img = image.resize(IMG_SIZE)
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    # ==========================
    # FRUIT PREDICTION (CNN OUTPUT)
    # ==========================

    try:
        fruit_prob = fruit_model.predict(img, verbose=0)[0][0]

        fruit = "🍎 Apple" if fruit_prob < 0.5 else "🍊 Orange"

    except Exception as e:
        st.error(f"Fruit model error: {e}")
        fruit = "Unknown"

    # ==========================
    # FEATURE EXTRACTION FOR QUALITY MODEL
    # ==========================

    try:
        image_features = feature_extractor.predict(img, verbose=0)

        # ==========================
        # QUALITY PREDICTION (SKLEARN)
        # ==========================

        quality_prediction = quality_model.predict(image_features)

        pred = quality_prediction[0]

        quality = "✅ Good Quality" if pred == 1 else "❌ Bad Quality"

    except Exception as e:
        st.error(f"Quality model error: {e}")
        quality = "Unknown"

    # ==========================
    # OUTPUT
    # ==========================

    st.success("Prediction Complete")

    st.write("### Fruit Type")
    st.write(fruit)

    st.write("### Quality")
    st.write(quality)