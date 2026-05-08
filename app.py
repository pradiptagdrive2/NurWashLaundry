import streamlit as st
from database import init_db

st.set_page_config(page_title="Laundry App", layout="wide")

init_db()

st.title("🧺 Sistem Kasir Laundry")
st.markdown("Selamat datang di aplikasi kasir laundry berbasis Streamlit")

st.info("Gunakan menu di sidebar untuk navigasi:")
