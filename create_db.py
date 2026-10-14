import sqlite3

conn = sqlite3.connect('cloth.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS clothing_items")
cursor.execute("""
CREATE TABLE clothing_items (
    id INTEGER,
    image TEXT,
    name TEXT,
    color TEXT,
    price INTEGER,
    brand TEXT
)
""")

# Yaha image ka naam sahi daal - yehi teri photo banegi
cursor.execute("INSERT INTO clothing_items VALUES (1, 'trekking.jpg', 'Trekking Jacket', 'Blue', 3500, 'Columbia')")
cursor.execute("INSERT INTO clothing_items VALUES (2, 'waterfall.jpg', 'Waterfall Jacket', 'Red', 2800, 'Wildcraft')")
cursor.execute("INSERT INTO clothing_items VALUES (3, 'hiking.jpg', 'Hiking Shirt', 'Green', 1500, 'Decathlon')")
cursor.execute("INSERT INTO clothing_items VALUES (4, 'dailywear.jpg', 'Dailywear Jacket', 'Black', 3000, 'Quechua')")

conn.commit()
conn.close()
print("Naya cloth.db ban gaya - with images!")