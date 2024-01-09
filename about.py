import streamlit as st
from set import set_background

def app():
    # Mengatur latar belakang website dengan gambar tertentu
    set_background('./pictures/background.png')
    # Menambahkan judul utama untuk halaman
    st.title('About Us :book:')
    # Garis pembatas untuk memisahkan bagian
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)
    # Subjudul untuk bagian yang menampilkan informasi tentang anggota tim
    st.subheader("Here are us:")
    # Membagi layar menjadi dua kolom
    col1, col2= st.columns(2)

    with col1:
        st.image("./pictures/Gybran.jpg")
        st.markdown("""
            <div style="text-align: center; font-weight: light; font-size: 18px;">
                Gybran Khairul Anam - 1402021026
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("./pictures/Rayhan.jpg")
        st.markdown("""
            <div style="text-align: center; font-weight: light; font-size: 18px;">
                Rayhan Alif Zahrandhika R - 1402021051
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)

    # Footer dengan hak cipta, menggunakan HTML untuk styling
    st.markdown("""
        <div style="text-align: center; font-weight: bold; font-size: 24px;">
            © EUREKA - 2024
        </div>
    """, unsafe_allow_html=True)
    

    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)