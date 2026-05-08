import sqlite3

def main():
    conn = sqlite3.connect("telecom.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY,
        service TEXT,
        issue TEXT,
        status TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS directory (
        id INTEGER PRIMARY KEY,
        department TEXT,
        contact_name TEXT,
        phone TEXT
    )
    """)

    tickets = [
        (1001, "Wireless", "Wireless outage", "Open"),
        (1002, "Mobile", "Phone activation", "Closed"),
        (1003, "Internet", "Slow connection", "Open"),
        (1004, "Wireless", "SIM issue", "Closed")
    ]

    directory_data = [
        (1, "IT", "John Smith", "410-555-1000"),
        (2, "Telecom", "Sarah Brown", "410-555-2000")
    ]

    cursor.executemany("INSERT INTO tickets VALUES (?, ?, ?, ?)", tickets)
    cursor.executemany("INSERT INTO directory VALUES (?, ?, ?, ?)", directory_data)

    conn.commit()
    conn.close()
    print("Data inserted successfully.")

if __name__ == "__main__":
    main()