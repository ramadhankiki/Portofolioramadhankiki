
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Portofolio RNR Rizky", layout="wide")

st.title("📊 Portofolio RNR Trading Rizky")

uploaded_file = st.file_uploader("Upload file Excel portofolio kamu (.xlsx)", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.success("✅ File berhasil dimuat!")
        st.dataframe(df, use_container_width=True)

        with st.expander("📈 Ringkasan Statistik"):
            st.write("Jumlah posisi:", len(df))
            st.write("Total modal:", df['Modal (Rp)'].sum())
            st.write("Total estimasi profit:", df['Target Profit (Rp)'].sum())

    except Exception as e:
        st.error(f"Gagal memuat file: {e}")

st.markdown("---")
st.markdown("📌 **Catatan:** Pastikan file memiliki kolom seperti 'Koin', 'Modal (Rp)', dan 'Target Profit (Rp)'.")
