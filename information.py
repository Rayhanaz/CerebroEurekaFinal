# Import streamlit dan library pendukung lainnya
import streamlit as st
from set import set_background
from PIL import Image

def app():
    # Mengatur latar belakang website dengan gambar tertentu
    set_background('./pictures/background.png')
    
    # Membuat judul utama aplikasi yang memberikan gambaran singkat tentang topik aplikasi.
    st.title("Information About Brain Tumor :brain:")
    # Garis horizontal untuk memisahkan bagian header dari konten lainnya.
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)

    # Bagian ini menyajikan informasi tentang dataset yang digunakan dalam aplikasi.
    st.subheader("What Is Brain Tumor?")
    # Deskripsi dataset yang digunakan, termasuk jumlah gambar dan klasifikasinya.
    st.write("A brain tumor is an abnormal growth or mass of cells in or around the brain. These tumors can be either malignant (cancerous) or benign (noncancerous). Primary brain tumors originate in the brain, while secondary or metastatic brain tumors spread to the brain from other parts of the body. There are more than 150 different types of brain tumors, with various subtypes including gliomas, meningiomas, pituitary adenomas, and schwannomas. Some brain tumors grow quickly, while others are slow-growing.")
    st.write("Brain tumors can cause a range of symptoms depending on their size, type, and location. Common symptoms include headaches, seizures, difficulty thinking or speaking, personality changes, weakness or paralysis on one side of the body, balance problems, vision and hearing issues, facial numbness or tingling, nausea or vomiting, and confusion​.")
    st.write("The exact causes of brain tumors are not fully understood, but they are believed to involve changes in brain cell DNA, possibly due to genetic and environmental factors. Certain inherited genetic syndromes are also associated with an increased risk of brain tumors​.")
    st.write("Brain tumors are diagnosed through a combination of neurological exams, imaging tests such as MRI and CT scans, and sometimes biopsies. Treatment options include surgery, radiation therapy, chemotherapy, targeted therapy, and immunotherapy, depending on the tumor's characteristics and the patient's overall health.")
    st.write("While brain tumors cannot be prevented, avoiding environmental hazards like smoking and excessive radiation exposure may reduce risk. The prognosis for brain tumor patients varies widely based on factors such as the tumor's type, grade, location, and whether it can be completely removed through surgery.")
    st.write("For detailed information, you can refer to the resources provided by:")
    st.write("- [Hopkins Medicine](https://www.hopkinsmedicine.org/health/conditions-and-diseases/brain-tumor)")
    # Footer dengan hak cipta, menggunakan HTML untuk styling
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; font-weight: bold; font-size: 24px;">
            © EUREKA - 2024
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)
