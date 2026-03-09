import sqlite3

def connect_db():
    conn = sqlite3.connect("secure_data.db")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_data(name, email):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))

    conn.commit()
    conn.close()


def get_all_data():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    conn.close()

    return data
