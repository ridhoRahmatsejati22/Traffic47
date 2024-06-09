import streamlit as st

def app():
    st.title("Selamat Datang di aplikasi [Traffic47] 🚀")
    st.markdown(
        """
        <div style="background-color:#f0f8ff;padding:10px;border-radius:10px">
        <p style="font-size:18px;color:#008080">Ini adalah halaman beranda dari aplikasi Traffic47. Aplikasi ini dirancang untuk membantu Anda menganalisis 
        dan memprediksi data dengan mudah dan cepat.</p>
        </div>
        """, unsafe_allow_html=True
    )

    st.header("Prediksi dan Analisis Data")
    st.markdown(
        """
        <div style="background-color:#f0f8ff;padding:10px;border-radius:10px">
        <p style="font-size:16px;color:#008080">**Prediksi:** Anda dapat menggunakan aplikasi ini untuk memprediksi data di masa depan berdasarkan data historis. 
          Hal ini dapat membantu Anda dalam merencanakan strategi atau membuat keputusan di masa depan.</p>
        <p style="font-size:16px;color:#008080">**Analisis Data:** Aplikasi ini memungkinkan Anda untuk melakukan analisis mendalam terhadap data, 
          sehingga Anda dapat memahami pola dan tren yang mungkin terjadi.</p>
        </div>
        """, unsafe_allow_html=True
    )

    st.header("Cara Kerja Aplikasi:")
    st.markdown(
        """
        <div style="background-color:#f0f8ff;padding:10px;border-radius:10px">
        <p style="font-size:16px;color:#008080">1. **Pilih Opsi:** Navigasi ke bagian yang Anda minati menggunakan sidebar di sebelah kiri.</p>
        <p style="font-size:16px;color:#008080">2. **Analisis atau Prediksi:** Pilih opsi "Analisis" untuk melakukan analisis data atau pilih "Prediksi" 
           untuk memprediksi data di masa depan.</p>
        <p style="font-size:16px;color:#008080">3. **Interaktif dan Mudah Dipahami:** Ikuti petunjuk di setiap halaman untuk menggunakan fitur-fitur aplikasi ini. 
           Anda akan melihat visualisasi data yang interaktif untuk membantu Anda memahami hasil analisis atau prediksi.</p>
        </div>
        """, unsafe_allow_html=True
    )

    st.header("Tentang Pembuat Aplikasi:")
    st.markdown(
        """
        <div style="background-color:#f0f8ff;padding:10px;border-radius:10px">
        <p style="font-size:16px;color:#008080">Aplikasi ini dibuat oleh tim pengembang yang berdedikasi. Anda dapat menghubungi kami melalui media sosial berikut:</p>
        <ul style="font-size:16px;color:#008080">
            <li><a href="https://www.linkedin.com/in/rido-rahmat-sejati" target="https://www.linkedin.com/in/rido-rahmat-sejati-b275942a6/" style="color:#008080;">Rido Rahmat Sejati - LinkedIn</a></li>
            <li><a href="https://www.facebook.com/rido.rahmat.sejati" target="_blank" style="color:#008080;">Rido Rahmat Sejati - Facebook</a></li>
            <li><a href="https://www.linkedin.com/in/bimo-ariansyah" target="_blank" style="color:#008080;">Bimo Ariansyah - LinkedIn</a></li>
            <li><a href="https://www.facebook.com/bimo.ariansyah" target="_blank" style="color:#008080;">Bimo Ariansyah - Facebook</a></li>
            <li><a href="https://www.linkedin.com/in/sallsabilla" target="_blank" style="color:#008080;">Sallsabilla - LinkedIn</a></li>
            <li><a href="https://www.facebook.com/sallsabilla" target="_blank" style="color:#008080;">Sallsabilla - Facebook</a></li>
            <li><a href="https://www.linkedin.com/in/muhammad-nabil-alrasyid" target="_blank" style="color:#008080;">Muhammad Nabil Alrasyid - LinkedIn</a></li>
            <li><a href="https://www.facebook.com/muhammad.nabil.alrasyid" target="_blank" style="color:#008080;">Muhammad Nabil Alrasyid - Facebook</a></li>
            <li><a href="https://www.linkedin.com/in/sarah-apriani" target="_blank" style="color:#008080;">Sarah Apriani - LinkedIn</a></li>
            <li><a href="https://www.facebook.com/sarah.apriani" target="_blank" style="color:#008080;">Sarah Apriani - Facebook</a></li>
        </ul>
        <p style="font-size:16px;color:#008080">Kami selalu terbuka untuk umpan balik dan saran untuk meningkatkan aplikasi ini. Terima kasih telah menggunakan Traffic47!</p>
        </div>
        """, unsafe_allow_html=True
    )

# Run the app function to display the dashboard
if __name__ == "__main__":
    app()
