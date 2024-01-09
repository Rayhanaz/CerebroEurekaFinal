import streamlit as st
import os
import pandas as pd
from PIL import Image
# Impor fungsi classify dari classification.py
from classification import classify, load_model

# Misalkan kita menyimpan riwayat dalam file CSV
history_file = 'upload_history.csv'

def load_history():
    if os.path.exists(history_file):
        return pd.read_csv(history_file)
    else:
        return pd.DataFrame(columns=['Filename', 'Upload Time', 'Classification Result', 'Confidence Score'])

def save_history(new_data):
    history_df = load_history()
    if not isinstance(new_data, pd.DataFrame):
        new_data = pd.DataFrame([new_data])
    history_df = pd.concat([history_df, new_data], ignore_index=True)
    history_df.to_csv(history_file, index=False)

def app():
    st.title('Demo Images :computer:')

    # Bagian untuk mengunggah gambar
    st.subheader('Upload a Brain MRI Image to here')
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a file...")
    if uploaded_file is not None:
        # Menampilkan gambar yang diunggah
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='Uploaded MRI Image', use_column_width=True)

        save_path = os.path.join('uploads', uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Muat model untuk klasifikasi
        model = load_model('./model/Xception.h5')
        with open('./model/labels.txt', 'r') as f:
            class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
            f.close()

        class_name, conf_score = classify(image, model, class_names)

        st.write("---")
        st.write("## Class: {}".format(class_name))
        st.write("### Confident Score: {:.2f}%".format(conf_score * 100))  # Format untuk dua desimal
        st.write("---")

        save_history({
            'Filename': uploaded_file.name,
            'Upload Time': pd.Timestamp.now(),
            'Classification Result': class_name,
            'Confidence Score': f"{conf_score * 100:.2f}%"
        })

        st.success('File uploaded and classified successfully!')

    # Menampilkan riwayat pengunggahan
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)
    st.subheader('History Images')
    history_df = load_history()

    # Tambahkan checkbox di setiap baris untuk memilih baris yang akan dihapus
    if not history_df.empty:
        selected_indices = st.multiselect("Select rows to delete", history_df.index)

        # Tombol untuk menghapus baris yang dipilih
        if st.button('Delete Selected Rows'):
            history_df = history_df.drop(selected_indices)
            history_df.to_csv(history_file, index=False)
            st.success('Selected rows deleted!')

    st.write(history_df)

    # Pindahkan tombol 'Clear History' ke bawah tabel
    if st.button('Clear History'):
        if os.path.exists(history_file):
            os.remove(history_file)
            st.success('History cleared!')
        else:
            st.error('No history file found.')

    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)

    # Footer dengan hak cipta aplikasi, menggunakan HTML untuk styling.
    st.markdown("""
        <div style="text-align: center; font-weight: bold; font-size: 24px;">
            © EUREKA - 2024
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)