from flask import Flask
import sqlite3

app = Flask(__name__)

def init_db():
    # Koneksi dan inisialisasi database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')
    cursor.execute("INSERT INTO visitors (name) VALUES ('Pengunjung Baru')")
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM visitors")
    count = cursor.fetchone()[0]
    conn.close()
    return count

@app.route('/')
def hello():
    total_visitors = init_db()
    return f"Halo dari Flask + Database SQLite + Docker + Jenkins! Total Kunjungan: {total_visitors}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
