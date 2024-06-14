# init_db.py
import sqlite3

def init_db():
    conn = sqlite3.connect('library.db')
    with open('schema.sql') as f:
        conn.executescript(f.read())
    conn.close()

if __name__ == "__main__":
    init_db()
