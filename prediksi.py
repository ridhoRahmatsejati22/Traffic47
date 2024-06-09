import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

def load_data(file_path):
    data = pd.read_csv(file_path)
    data['order_date'] = pd.to_datetime(data['order_date']).dt.date
    data['day_of_week'] = pd.to_datetime(data['order_date']).dt.dayofweek
    data['month'] = pd.to_datetime(data['order_date']).dt.month
    data['year'] = pd.to_datetime(data['order_date']).dt.year
    return data

def build_regression_model(data):
    if len(data) == 0:
        st.write("Tidak ada data yang tersedia untuk membuat model.")
        return None

    X = data[['day_of_week', 'month', 'year']]
    y = data['quantity']

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_sales(model, selected_sku, selected_start_date, selected_end_date):
    # Buat data untuk prediksi bulan ini
    this_month_start = pd.to_datetime(selected_start_date)
    this_month_end = pd.to_datetime(selected_end_date)
    this_month_prediction_dates = pd.date_range(start=this_month_start, end=this_month_end)
    this_month_prediction_data = pd.DataFrame({'order_date': this_month_prediction_dates})
    this_month_prediction_data['day_of_week'] = this_month_prediction_data['order_date'].dt.dayofweek
    this_month_prediction_data['month'] = this_month_prediction_data['order_date'].dt.month
    this_month_prediction_data['year'] = this_month_prediction_data['order_date'].dt.year

    # Lakukan prediksi bulan ini menggunakan model
    this_month_predicted_sales = model.predict(this_month_prediction_data[['day_of_week', 'month', 'year']])

    # Buat data untuk prediksi bulan sebelumnya
    last_month_start = this_month_start - pd.DateOffset(months=1)
    last_month_end = this_month_end - pd.DateOffset(months=1)
    last_month_prediction_dates = pd.date_range(start=last_month_start, end=last_month_end)
    last_month_prediction_data = pd.DataFrame({'order_date': last_month_prediction_dates})
    last_month_prediction_data['day_of_week'] = last_month_prediction_data['order_date'].dt.dayofweek
    last_month_prediction_data['month'] = last_month_prediction_data['order_date'].dt.month
    last_month_prediction_data['year'] = last_month_prediction_data['order_date'].dt.year

    # Lakukan prediksi bulan sebelumnya menggunakan model
    last_month_predicted_sales = model.predict(last_month_prediction_data[['day_of_week', 'month', 'year']])

    # Tampilkan hasil prediksi
    st.write(f"Prediksi Penjualan Produk {selected_sku}:")
    st.write("Bulan Ini:", this_month_predicted_sales)
    st.write("Bulan Sebelumnya:", last_month_predicted_sales)

    # Penilaian prediksi
    difference = this_month_predicted_sales - last_month_predicted_sales
    assessment = "Prediksi Bagus" if all(difference >= 0) else "Prediksi Buruk"
    st.write(f"Hasil Prediksi: {assessment}")

def app():
    st.title("Prediksi Penjualan Produk")

    # Memuat dataset
    file_path = 'women_clothing_ecommerce_sales.csv'
    data = load_data(file_path)

    # Menampilkan pilihan SKU produk
    sku_options = sorted(data['sku'].unique())
    selected_sku = st.selectbox("Pilih SKU Produk:", sku_options)

    # Menampilkan rentang tanggal
    min_date = data['order_date'].min()
    max_date = data['order_date'].max()
    selected_start_date = st.date_input("Pilih Tanggal Awal:", min_value=min_date, max_value=max_date, value=min_date)
    selected_end_date = st.date_input("Pilih Tanggal Akhir:", min_value=min_date, max_value=max_date, value=max_date)

    # Filter data berdasarkan SKU dan rentang tanggal
    filtered_data = data[(data['sku'] == selected_sku) & (data['order_date'] >= selected_start_date) & (data['order_date'] <= selected_end_date)]

    # Bangun model regresi
    regression_model = build_regression_model(filtered_data)

    if regression_model is not None:
        # Lakukan prediksi penjualan jika model berhasil dibangun
        if st.button("Prediksi"):
            predict_sales(regression_model, selected_sku, selected_start_date, selected_end_date)

if __name__ == "__main__":
    app()
