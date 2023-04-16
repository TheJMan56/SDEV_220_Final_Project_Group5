import sqlite3

conn = sqlite3.connect('Inventory.db')
curs = conn.cursor()

curs.execute('SELECT * FROM Inventory')
rows = curs.fetchall()

print(rows)

for row in rows:
    print(row[1])
