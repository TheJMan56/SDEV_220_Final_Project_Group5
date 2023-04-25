import sqlite3

conn = sqlite3.connect('Inventory_and_Users_and_Orders.db')
curs = conn.cursor()

curs.execute('SELECT * FROM Users')
rows = curs.fetchall()

print(rows)

for row in rows:
    print(row[1])

conn.close()
