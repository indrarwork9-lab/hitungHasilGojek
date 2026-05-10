import streamlit as st

st.set_page_config(
    page_title="Hitung Hasil Gojek",
    page_icon="🏍️",
    layout="centered"
)

st.title("🏍️ Hitung Hasil Gojek")
st.write("Aplikasi untuk menghitung pembagian pendapatan driver Gojek")

st.divider()

cash = st.number_input(
    "Pendapatan Cash (Rp)",
    min_value=0,
    step=1000
)

qris = st.number_input(
    "Pendapatan QRIS (Rp)",
    min_value=0,
    step=1000
)

pendapatan = cash + qris

st.write(f"Total Pendapatan: Rp {pendapatan:,.0f}")

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

if pendapatan > 0:
    bensin = pendapatan * persen_bensin / 100
    servis = pendapatan * persen_servis / 100
    sisa = pendapatan - bensin - servis

    st.subheader("📊 Hasil Perhitungan")

    st.success(f"Pendapatan Harian: Rp {pendapatan:,.0f}")
    st.info(f"Biaya Bensin: Rp {bensin:,.0f}")
    st.warning(f"Dana Servis: Rp {servis:,.0f}")
    st.subheader(f"💰 Sisa Uang: Rp {sisa:,.0f}")

    st.divider()

    st.subheader("📅 Simulasi Bulanan")

    hari_kerja = st.number_input(
        "Jumlah Hari Kerja per Bulan",
        min_value=1,
        max_value=31,
        value=26
    )

    total_bulanan = pendapatan * hari_kerja
    total_bensin = bensin * hari_kerja
    total_servis = servis * hari_kerja
    total_sisa = sisa * hari_kerja

    st.write(f"Total Pendapatan Bulanan: Rp {total_bulanan:,.0f}")
    st.write(f"Total Bensin Bulanan: Rp {total_bensin:,.0f}")
    st.write(f"Total Dana Servis: Rp {total_servis:,.0f}")
    st.subheader(f"💵 Estimasi Uang Bersih: Rp {total_sisa:,.0f}")

st.divider()

st.caption("Dibuat untuk membantu Rizky Adi  mengatur keuangan harian")
