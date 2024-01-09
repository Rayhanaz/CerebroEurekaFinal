import streamlit as st
import tensorflow as tf
from keras.models import load_model
from PIL import Image
import numpy as np
import logging #untuk memonitoring dan debugging website saat pengembangan atau produksi.

from set import classify, set_background

# Mengaktifkan logging untuk memudahkan debugging dan melacak aktivitas.
logging.basicConfig(level=logging.INFO)

# Fungsi untuk preprocessing gambar yang diupload, penting untuk memastikan gambar diolah sesuai dengan yang model butuhkan.
def preprocess_image(image):
    # Logging ukuran gambar asli
    logging.info(f"Original image size: {image.size}")

    # Resize gambar ke ukuran yang dibutuhkan model
    image = image.resize((224, 224))
    logging.info(f"Resized image size: {image.size}")

    # Mengubah gambar menjadi array numpy dan normalisasi piksel
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    # Logging bentuk gambar yang telah diproses
    logging.info(f"Processed image shape: {image.shape}")

    return image

# Fungsi untuk klasifikasi gambar
def classify(image, model, class_names):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    prediction = prediction.flatten()

    # Mendapatkan id dan nama kelas dengan skor kepercayaan tertinggi
    class_id = np.argmax(prediction)
    class_name = class_names[class_id]
    conf_score = prediction[class_id]

    # Logging prediksi dan skor kepercayaan
    logging.info(f"Predicted class: {class_name}, Confidence score: {conf_score}")

    return class_name, conf_score