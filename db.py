import sqlite3

conn = sqlite3.connect('cloth.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS clothing_items")

cursor.execute("""
CREATE TABLE clothing_items (
    id INTEGER PRIMARY KEY,
    image_path TEXT,
    name TEXT,
    color TEXT,
    price INTEGER,
    brand TEXT
)
""")
cursor.execute("CREATE TABLE IF NOT EXISTS clothing_items (id INTEGER, image TEXT, name TEXT, price INTEGER, brand TEXT)")

cursor.execute("INSERT INTO clothing_items VALUES (1, 'Trekking Jacket', 'Blue', 3500, 'Columbia')")
cursor.execute("INSERT INTO clothing_items VALUES (2, 'Waterfall Jacket', 'Red', 2800, 'Wildcraft')")
cursor.execute("INSERT INTO clothing_items VALUES (3, 'Hiking Shirt', 'Green', 1500, 'Decathlon')")
cursor.execute("INSERT INTO clothing_items VALUES (4, 'DailyWear Jacket', 'Yellow', 2000, 'Quechua')")

conn.commit()
conn.close()
print("cloth.db ban gaya! ✅")