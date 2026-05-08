import sqlite3

def init_db():
    conn = sqlite3.connect("telecom.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tickets (
                        id INTEGER PRIMARY KEY,
                        service TEXT,
                        issue TEXT,
                        status TEXT
                      )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS directory (
                        id INTEGER PRIMARY KEY,
                        department TEXT,
                        contact_name TEXT,
                        phone TEXT
                      )''')
    conn.commit()
    conn.close()

def run_query(query, params=()):
    conn = sqlite3.connect("telecom.db")
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results
