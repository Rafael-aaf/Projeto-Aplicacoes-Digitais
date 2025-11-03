import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT NOT NULL,
    name TEXT NOT NULL,
    color TEXT NOT NULL,
    weight TEXT NOT NULL,
    height TEXT NOT NULL,
    ability TEXT NOT NULL
)
""")
conn.commit()
conn.close()

def inserir_pokemon(number, name, color, weight, height, ability):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuarios (number, name, color, weight, height, ability)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (number, name, color, weight, height, ability))
    conn.commit()
    conn.close()