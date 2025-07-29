
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Portofolio Crypto Ramadhan", layout="wide")

st.title("📊 Portofolio Crypto Ramadhan")
st.caption("Update dimulai sejak 27 Juli 2025")

# Upload file
uploaded_file = st.file_uploader("Upload file portofolio (.xlsx atau .csv)", type=["xlsx", "csv"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file, sheet_name="Riwayat")
        else:
            df = pd.read_csv(uploaded_file)

        st.subheader("📌 Ringkasan Portofolio")
        total_investasi = df['Investasi (Rp)'].sum()
        total_profit = df['Profit (Rp)'].sum()
        total_presentase = df['% Profit'].mean()

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Investasi", f"Rp {total_investasi:,.0f}")
        col2.metric("Total Profit", f"Rp {total_profit:,.0f}")
        col3.metric("Rata-rata Profit", f"{total_presentase:.2f} %")

        df_aktif = df[df['Kategori'] == 'Aktif']
        df_listing = df[df['Kategori'] == 'Listing']

        st.subheader("📌 Koin Aktif")
        st.dataframe(df_aktif, use_container_width=True)

        st.subheader("📌 Koin Listing")
        st.dataframe(df_listing, use_container_width=True)

        st.subheader("📈 Grafik Performa Harian")
        chart_data = df[['Tanggal', 'Nama Koin', '% Profit']]
        chart = alt.Chart(chart_data).mark_line(point=True).encode(
            x='Tanggal:T',
            y='% Profit:Q',
            color='Nama Koin:N',
            tooltip=['Nama Koin', 'Tanggal', '% Profit']
        ).interactive()

        st.altair_chart(chart, use_container_width=True)

        st.info("📝 Catatan: File `.xlsx` harus punya sheet bernama `Riwayat`. File `.csv` langsung dibaca barisnya.")

    except Exception as e:
        st.error(f"Gagal membaca file. Error: {str(e)}")
else:
    st.warning("Silakan upload file Excel atau CSV portofoliomu terlebih dahulu.")
