# Import library yang dibutuhkan
import base64 #untuk mengubah data biner menjadi teks ASCII.
import streamlit as st
from PIL import ImageOps, Image
import numpy as np

def set_background(image_file):
    """
    Fungsi ini mengatur latar belakang aplikasi Streamlit menjadi gambar yang ditentukan oleh file gambar yang diberikan.

    Parameters:
        image_file (str): Path ke file gambar yang akan digunakan sebagai latar belakang.

    Returns:
        None
    """
    # Membuka file gambar dan membacanya
    with open(image_file, "rb") as f:
        img_data = f.read()

    # Melakukan encoding data gambar menjadi base64
    b64_encoded = base64.b64encode(img_data).decode()

    # Membuat dan mengaplikasikan style CSS untuk menetapkan gambar sebagai latar belakang
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

def classify(image, model, class_names):
    """
    Fungsi ini mengambil gambar, model, dan daftar nama kelas, lalu mengembalikan kelas yang diprediksi dan skor kepercayaan dari gambar tersebut.

    Parameters:
        image (PIL.Image.Image): Gambar yang akan diklasifikasikan.
        model (tensorflow.keras.Model): Model pembelajaran mesin yang telah dilatih untuk klasifikasi gambar.
        class_names (list): Daftar nama kelas yang sesuai dengan kelas yang dapat diprediksi oleh model.

    Returns:
        Tuple dari nama kelas yang diprediksi dan skor kepercayaan untuk prediksi tersebut.
    """
    # Mengubah ukuran gambar menjadi (224, 224)
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

    # Mengonversi gambar menjadi array numpy
    image_array = np.asarray(image)

    # Normalisasi gambar
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Menyiapkan input model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # Melakukan prediksi
    prediction = model.predict(data)
    # Mendapatkan indeks dengan skor tertinggi (menggunakan threshold 0.95)
    index = 0 if prediction[0][0] > 0.95 else 1
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name, confidence_score