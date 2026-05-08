import streamlit as st
from datetime import datetime, timedelta
from database import get_connection
from utils import generate_nota, generate_struk, generate_wa_link

st.title("📋 Transaksi Baru")

nama = st.text_input("Nama")
hp = st.text_input("No HP")
layanan = st.text_input("Layanan", "Trial")
harga = st.number_input("Harga per Kg", value=4750)
berat = st.number_input("Berat", value=1.0)
estimasi_hari = st.number_input("Estimasi Hari", value=2)
status = st.selectbox("Status", ["Proses", "Dicuci", "Selesai"])
pembayaran = st.selectbox("Pembayaran", ["lunas", "belum lunas"])
catatan = st.text_area("Catatan")

if st.button("Simpan Transaksi"):
    now = datetime.now()
    est = now + timedelta(days=int(estimasi_hari))
    total = harga * berat
    nota = generate_nota()

    data = {
        "nota": nota,
        "nama": nama,
        "hp": hp,
        "layanan": layanan,
        "harga": harga,
        "berat": berat,
        "total": total,
        "status": status,
        "pembayaran": pembayaran,
        "tanggal": now.strftime("%Y-%m-%d %H:%M:%S"),
        "estimasi": est.strftime("%Y-%m-%d"),
        "estimasi_hari": estimasi_hari,
        "catatan": catatan
    }

    conn = get_connection()
    c = conn.cursor()
    c.execute("""
    INSERT INTO transaksi 
    (nota,nama,hp,layanan,harga,berat,total,status,pembayaran,tanggal,estimasi,catatan)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        data["nota"], data["nama"], data["hp"], data["layanan"],
        data["harga"], data["berat"], data["total"], data["status"],
        data["pembayaran"], data["tanggal"], data["estimasi"], data["catatan"]
    ))
    conn.commit()

    struk = generate_struk(data)

    st.success("Transaksi berhasil!")
    st.text_area("Struk", struk, height=400)

    wa = generate_wa_link(hp, struk)
    st.link_button("Kirim ke WhatsApp", wa)
