import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    data = pd.read_csv(file_path)
    data['order_date'] = pd.to_datetime(data['order_date'])
    return data

def plot_sales_over_time(data, sku):
    product_data = data[data['sku'] == sku]
    plt.figure(figsize=(10, 6))
    plt.plot(product_data['order_date'], product_data['quantity'], marker='o', linestyle='-')
    plt.title(f'Penjualan Produk {sku} Seiring Waktu')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Terjual')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

def app():
    st.title("Analisis Penjualan Produk")

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

    # Konversi tanggal menjadi datetime64[ns]
    selected_start_date = pd.to_datetime(selected_start_date)
    selected_end_date = pd.to_datetime(selected_end_date)

    # Filter data berdasarkan SKU dan rentang tanggal
    filtered_data = data[(data['sku'] == selected_sku) & (data['order_date'] >= selected_start_date) & (data['order_date'] <= selected_end_date)]

    # Plot penjualan produk terpilih seiring waktu
    plot_sales_over_time(filtered_data, selected_sku)

    # Menampilkan total penjualan produk terpilih
    total_sales = filtered_data['quantity'].sum()
    st.write(f"Total Penjualan Produk {selected_sku} dari {selected_start_date} hingga {selected_end_date}: {total_sales}")

if __name__ == "__main__":
    app()
