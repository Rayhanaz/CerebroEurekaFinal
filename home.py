import streamlit as st
from set import set_background
from PIL import Image

def app():
    # Mengatur latar belakang website dengan gambar tertentu
    set_background('./pictures/background.png')
    
    # Judul utama untuk landing page
    st.title("Welcome to CerebroEureka :brain:")

    # Deskripsi singkat tentang aplikasi
    st.subheader("CerebroEureka is an advanced AI-based platform for classifying brain tumors using MRI data.")

    st.image('./pictures/Home.png')
    st.markdown("""
        <div style="text-align: center; font-weight: light; font-size: 24px;">
            Explore our website on sidebar
        </div>
    """, unsafe_allow_html=True)
    # Menambahkan konten untuk masing-masing bagian
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)
    # Footer dengan hak cipta aplikasi, menggunakan HTML untuk styling.
    st.markdown("""
        <div style="text-align: center; font-weight: bold; font-size: 24px;">
            © EUREKA - 2024
        </div>
    """, unsafe_allow_html=True)

    # Separator akhir untuk footer.
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)
