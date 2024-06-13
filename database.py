# my_cli_app/database.py

import sqlite3

DATABASE_URL = "library.db"

def init_db():
    with sqlite3.connect(DATABASE_URL) as conn:
        with open('schema.sql') as f:
            conn.executescript(f.read())

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn
