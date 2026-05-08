from datetime import datetime
import urllib.parse

def format_rupiah(x):
    return f"Rp{int(x):,}".replace(",", ".")

def generate_nota():
    return f"CUTSX/{int(datetime.now().timestamp())}"

def generate_struk(data):
    return f"""
WashTrial
------------------------------
No Nota : #{data['nota']}
Tanggal : {data['tanggal']}
Pembayaran : {data['pembayaran']}
Status : {data['status']}
Nama : {data['nama']} ({data['hp']})
Est : {data['estimasi_hari']} Hari {data['estimasi']}
Note : {data['catatan']}
----------------------------
{data['layanan']} {data['berat']} Kg ({format_rupiah(data['harga'])} x {data['berat']}Kg)
{format_rupiah(data['total'])}
------------------------------
SubTotal : {format_rupiah(data['total'])}
Total : {format_rupiah(data['total'])}
Bayar : {format_rupiah(data['total'])}

------------------------------

Cek status laundry anda dengan mengklik link :
https://yourapp.streamlit.app/?nota={data['nota']}
"""

def generate_wa_link(phone, message):
    encoded = urllib.parse.quote(message)
    return f"https://wa.me/{phone}?text={encoded}"
