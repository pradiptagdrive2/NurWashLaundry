import streamlit as st
import pandas as pd
from database import get_connection

st.title("📜 Riwayat Transaksi")

conn = get_connection()
df = pd.read_sql("SELECT * FROM transaksi ORDER BY id DESC", conn)

st.dataframe(df)
