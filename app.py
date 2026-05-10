import streamlit as st

st.set_page_config(
    page_title="Hitung Hasil Gojek",
    page_icon="🏍️",
    layout="centered"
)

st.title("🏍️ Hitung Hasil Gojek")
st.write("Aplikasi sederhana untuk menghitung pembagian pendapatan driver Gojek")

st.divider()

pendapatan = st.number_input(
    "Masukkan Pendapatan Harian (Rp)",
    min_value=0,
    step=1000
)

persen_bensin = st.slider(
    "Persentase Bensin (%)",
    0,
    50,
    25
)

persen_servis = st.slider(
    "Persentase Servis (%)",
    0,
    30,
    10
)
