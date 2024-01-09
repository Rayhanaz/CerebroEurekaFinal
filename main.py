import streamlit as st
import home, about, information, demo, dataset
from set import set_background

# Mengatur konfigurasi halaman dasar website Streamlit
st.set_page_config(page_title="CerebroEureka", page_icon=":brain:")

class MultiApp:
    def __init__(self):
        # Inisialisasi daftar untuk menyimpan apps yang berbeda
        self.apps = []

    def add_app(self, title, func):
        """ Add a new application. """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        """ Run the app. """
        with st.sidebar:
            # Mengatur latar belakang dan logo di sidebar
            set_background('./pictures/background.png')
            st.image('./pictures/Logo-Eureka.png', width=150)

            # Mengatur gaya untuk logo di sidebar
            st.markdown("""
                <style>
                .sidebar .sidebar-content img {
                    border-radius: 50%;  # Make logo edges round
                }
                </style>
                """, unsafe_allow_html=True)
            
            # Membuat menu navigasi menggunakan radio buttons
            app = st.radio(
                'Menu',
                ['Home', 'Dataset', 'Information', 'Test', 'About Us']
            )

        # Routing ke halaman berdasarkan pilihan pengguna
        if app == "Home":
            home.app()
        elif app == "Dataset":
            dataset.app()
        elif app == "Information":
            information.app()
        elif app == "Test":
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

# Menjalankan website jika skrip dijalankan sebagai program utama
if __name__ == "__main__":
    app = MultiApp()
    app.run()
