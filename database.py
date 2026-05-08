import sqlite3

DB_NAME = "data/laundry.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def init_db():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS pelanggan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        hp TEXT UNIQUE,
        alamat TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS transaksi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nota TEXT,
        nama TEXT,
        hp TEXT,
        layanan TEXT,
        harga REAL,
        berat REAL,
        total REAL,
        status TEXT,
        pembayaran TEXT,
        tanggal TEXT,
        estimasi TEXT,
        catatan TEXT
    )
    """)

    conn.commit()
    conn.close()
