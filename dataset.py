import streamlit as st
from PIL import Image

def app():
    # Membuat judul utama aplikasi yang memberikan gambaran singkat tentang topik aplikasi.
    st.title("Brain Tumor MRI Dataset :bar_chart:")
    # Garis horizontal untuk memisahkan bagian header dari konten lainnya.
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)
    st.subheader("What is MRI?")
    st.write("An MRI (Magnetic Resonance Imaging) is a diagnostic test that produces highly detailed images of the organs and structures within the body. It utilizes a large magnet, radio waves, and a computer to generate these images, distinguishing itself from other imaging techniques like X-rays or CT scans by not using radiation. MRI is particularly effective in imaging non-bony parts or soft tissues and provides clearer images of the brain, spinal cord, nerves, muscles, ligaments, and tendons compared to X-rays and CT scans. This makes it a safer and often more preferable option for examining certain internal structures")
    st.write("For detailed information, you can refer to the resources provided by:")
    st.write("- [Cleven Clinic](https://my.clevelandclinic.org/health/diagnostics/4876-magnetic-resonance-imaging-mri)")
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)

    # Bagian ini menyajikan informasi tentang dataset yang digunakan dalam aplikasi.
    st.subheader("Dataset Information")
    # Deskripsi dataset yang digunakan, termasuk jumlah gambar dan klasifikasinya.
    st.write("We use a public dataset from Kaggle: the Brain Tumor MRI Dataset by MASOUD NICKPARVAR. This dataset combines three sources and contains 7023 images of human brain MRI, classified into four classes: glioma, meningioma, no tumor, and pituitary.")
    # Menyediakan link untuk sumber data tambahan.
    st.markdown("""
        - [Figshare Dataset by Jun Cheng](https://figshare.com/articles/dataset/brain_tumor_dataset/1512427)
        - [Kaggle Dataset by Sartaj Bhuvaji, et al](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri)
        - [Kaggle Dataset by AHMED HAMADA (Br35H)](https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection?select=no)
        """)
    # Tautan ke dataset utama untuk informasi lebih lanjut.
    st.write("For complete information, please click the link below:")
    st.markdown("- [Kaggle Dataset by MASOUD NICKPARVAR](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset/data)")
    # Separator untuk memisahkan bagian dataset dengan bagian berikutnya.
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)

    # Menampilkan informasi tentang kelas-kelas yang ada dalam dataset.
    st.subheader("Classes in this dataset:")

    col1, col2, col3, col4= st.columns(4)

    with col1:
        st.image("./pictures/glioma.jpg")
        st.markdown("""
            <div style="text-align: center; font-weight: light; font-size: 18px;">
                Glioma
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("./pictures/meningioma.jpg")
        st.markdown("""
            <div style="text-align: center; font-weight: light; font-size: 18px;">
                Meningioma
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.image("./pictures/Notumor.jpg")
        st.markdown("""
            <div style="text-align: center; font-weight: light; font-size: 18px;">
                No Tumor
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.image("./pictures/Pituitary.jpg")
        st.markdown("""
            <div style="text-align: center; font-weight: light; font-size: 18px;">
                Pituitary
            </div>
        """, unsafe_allow_html=True)

    # Separator untuk memisahkan bagian kelas dataset dengan footer.    
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)

    # Footer dengan hak cipta aplikasi, menggunakan HTML untuk styling.
    st.markdown("""
        <div style="text-align: center; font-weight: bold; font-size: 24px;">
            © EUREKA - 2024
        </div>
    """, unsafe_allow_html=True)

    # Separator akhir untuk footer.
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)
