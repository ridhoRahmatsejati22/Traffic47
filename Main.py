import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from Dashboard import show_dashboard  # Mengimpor fungsi show_dashboard dari modul Dashboard
from streamlit_lottie import st_lottie
import requests
import json

# Inisialisasi aplikasi Firebase
cred = credentials.Certificate('traffic-310ed-2f6a40409697.json')
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Firebase Web API Key
WEB_API_KEY = "AIzaSyBX1V3LAxpJI2Q0pTCSD6kZvKkZRHE-n4M"

# Fungsi untuk memuat animasi Lottie dari URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    st.set_page_config(page_title="Traffic47")  # Mengatur konfigurasi halaman sekali saja

    welcome_message = st.empty()  # Placeholder untuk pesan selamat datang
    login_message = st.empty()  # Placeholder untuk pesan sukses login

    # Inisialisasi variabel state session
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if 'dashboard' not in st.session_state:
        st.session_state.dashboard = False
    if 'rerun' not in st.session_state:
        st.session_state.rerun = False

    def login():
        email = st.session_state.get('login_email', '')
        password = st.session_state.get('login_password', '')

        if not email:
            st.warning('Mohon masukkan alamat email Anda.')
            return

        if not password:
            st.warning('Mohon masukkan password Anda.')
            return

        try:
            # Menggunakan Firebase Authentication REST API untuk verifikasi email dan password
            response = requests.post(
                f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={WEB_API_KEY}",
                data=json.dumps({"email": email, "password": password, "returnSecureToken": True}),
                headers={"Content-Type": "application/json"}
            )
            if response.status_code == 200:
                user_data = response.json()
                st.session_state.username = user_data['localId']
                st.session_state.useremail = user_data['email']
                st.session_state.dashboard = True  # Mengatur status dashboard ke True setelah login berhasil
                st.session_state.rerun = True  # Set the rerun flag to True
            else:
                st.warning('Login Gagal: Email atau password yang Anda masukkan salah.')
        except Exception as e:
            st.warning(f'Login Gagal: {e}')

    def register():
        email = st.session_state['signup_email']
        password = st.session_state['signup_password']
        username = st.session_state['signup_username']

        if not email:
            st.warning('Mohon masukkan alamat email Anda.')
            return

        if not username:
            st.warning('Mohon masukkan nama pengguna Anda.')
            return

        if not password:
            st.warning('Mohon masukkan password Anda.')
            return

        if len(password) < 6:
            st.warning('Password harus terdiri dari minimal 6 karakter.')
            return

        try:
            # Menggunakan Firebase Authentication REST API untuk membuat pengguna baru
            response = requests.post(
                f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={WEB_API_KEY}",
                data=json.dumps({"email": email, "password": password, "returnSecureToken": True}),
                headers={"Content-Type": "application/json"}
            )
            if response.status_code == 200:
                user_data = response.json()
                st.success('Akun berhasil dibuat!')
                st.markdown('Silakan login menggunakan email dan password Anda')
                st.balloons()
            else:
                st.warning('Pembuatan akun gagal: Email mungkin sudah terdaftar.')
        except Exception as e:
            st.warning(f'Pembuatan akun gagal: {e}')

    def logout():
        st.session_state.dashboard = False  # Mengatur status dashboard ke False saat logout
        st.session_state.username = ''
        st.session_state.useremail = ''
        st.session_state.rerun = True  # Set the rerun flag to True

    if st.session_state.rerun:
        st.session_state.rerun = False
        st.rerun()

    if st.session_state.dashboard:
        show_dashboard()  # Memanggil fungsi show_dashboard langsung dari Dashboard.py
    else:
        welcome_message.title('Selamat datang di aplikasi [Traffic47] :rocket:')

        # Menampilkan animasi Lottie di halaman login dan sign-up
        lottie_coding = load_lottieurl("https://lottie.host/6760c3f5-e83b-458b-8f47-f399d51b884f/sV794p0TH8.json")
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")

        choice = st.selectbox('Login/Signup', ['Login', 'Signup'])

        if choice == 'Login':
            st.text_input('Alamat Email', key='login_email')
            st.text_input('Password', type='password', key='login_password')
            st.button('Login', on_click=login)
        else:
            st.text_input('Alamat Email', key='signup_email')
            st.text_input('Masukkan nama pengguna unik Anda', key='signup_username')
            st.text_input('Password (minimal 6 karakter)', type='password', key='signup_password')
            st.button('Buat Akun Saya', on_click=register)

if __name__ == "__main__":
    main()
