import sqlite3

conn = sqlite3.connect('Inventory_and_Users.db')
curs = conn.cursor()

curs.execute('SELECT * FROM Inventory')
rows = curs.fetchall()

print(rows)

for row in rows:
    print(row[1])

curs.execute('SELECT * FROM Users')
rows = curs.fetchall()

print(rows)

for row in rows:
    print(row[1])

conn.close()
