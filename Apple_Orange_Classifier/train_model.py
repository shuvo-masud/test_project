import tensorflow as tf
import numpy as np
import os
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.utils import shuffle

# ---------------- PATHS ----------------
base_path = os.path.join(os.getcwd(), "Dataset")

trainA_path = os.path.join(base_path, "Train", "Apple")
trainB_path = os.path.join(base_path, "Train", "Orange")

testA_path = os.path.join(base_path, "Test", "Apple")
testB_path = os.path.join(base_path, "Test", "Orange")

img_size = (128, 128)

# ---------------- LOAD FUNCTION ----------------
def load_images(folder, label):
    data = []
    labels = []

    for file in os.listdir(folder):
        img_path = os.path.join(folder, file)

        img = keras.utils.load_img(img_path, target_size=img_size)
        img = keras.utils.img_to_array(img) / 255.0

        data.append(img)
        labels.append(label)

    return np.array(data), np.array(labels)

# ---------------- LOAD DATA ----------------
x_train_A, y_train_A = load_images(trainA_path, 0)
x_train_B, y_train_B = load_images(trainB_path, 1)

x_test_A, y_test_A = load_images(testA_path, 0)
x_test_B, y_test_B = load_images(testB_path, 1)

# ---------------- MERGE DATA ----------------
x_train = np.concatenate([x_train_A, x_train_B])
y_train = np.concatenate([y_train_A, y_train_B])

x_test = np.concatenate([x_test_A, x_test_B])
y_test = np.concatenate([y_test_A, y_test_B])

# ---------------- SHUFFLE ----------------
x_train, y_train = shuffle(x_train, y_train, random_state=42)
x_test, y_test = shuffle(x_test, y_test, random_state=42)

# ---------------- MODEL ----------------
model = keras.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# ---------------- COMPILE ----------------
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# ---------------- TRAIN ----------------
model.fit(
    x_train, y_train,
    validation_data=(x_test, y_test),
    epochs=10,
    batch_size=32
)

# ---------------- EVALUATE ----------------
loss, acc = model.evaluate(x_test, y_test)
print("Accuracy:", acc)

# ---------------- SAVE ----------------
model.save("apple_orange_model.keras")
print("Model saved successfully!")