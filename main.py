import streamlit as st
from streamlit_option_menu import option_menu
import home, about, information, demo, dataset
from set import set_background

# Konfigurasi dasar untuk halaman Streamlit
st.set_page_config(page_title="CerebroEureka", page_icon=":brain:")

class MultiApp:
    def __init__(self):
        # Membuat daftar untuk menyimpan berbagai aplikasi
        self.apps = []

    def add_app(self, title, func):
        # Menambahkan aplikasi baru ke dalam daftar
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Fungsi untuk menjalankan aplikasi berdasarkan pilihan di sidebar
        with st.sidebar:
            # Mengatur latar belakang dan logo di sidebar
            set_background('./pictures/background.png')
            st.image('./pictures/cerebroeureka.png', width=150)
            # Mengatur gaya untuk logo di sidebar
            st.markdown("""
                <style>
                .sidebar .sidebar-content img {
                    border-radius: 50%;  # Membuat tepi gambar menjadi bulat
                }
                </style>
                """, unsafe_allow_html=True)
            
            # Membuat menu navigasi dengan berbagai opsi
            app = option_menu(
                menu_title='Menu',
                options=['Home', 'Dataset', 'Information', 'Demo', 'About Us'],
                icons=['house-fill','clipboard-data-fill', 'info-circle-fill', 'tags-fill', 'file-person-fill'],
                menu_icon='cast',
                default_index=0,
                orientation='vertical',
                styles={
                    "container": {"padding": "5!important", "background-color": "white"},
                    "icon": {"color": "bold black", "font-size": "23px"}, 
                    "nav-link": {"color": "black", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "#90EE90"},
                    "nav-link-selected": {"background-color": "#90EE90"},
                }
            )

        # Routing ke halaman yang dipilih pengguna dari sidebar
        if app == "Home":
            home.app()
        elif app == "Dataset":
            dataset.app()
        elif app == "Information":
            information.app()
        elif app == "Demo":
            demo.app()
        elif app == "About Us":
            about.app()

        # Menambahkan footer di sidebar
        st.sidebar.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)
        st.sidebar.markdown("""
        <div style="text-align: center; font-weight: bold; font-size: 20px;">
            © EUREKA - 2024
        </div>
    """, unsafe_allow_html=True)

# Menjalankan aplikasi jika skrip ini
if __name__ == "__main__":
    app = MultiApp()
    app.run()
