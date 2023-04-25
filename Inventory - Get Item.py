import sqlite3

conn = sqlite3.connect('Inventory_and_Users_and_Orders.db')
curs = conn.cursor()

curs.execute('SELECT * FROM Inventory')
rows = curs.fetchall()

print(rows)

for row in rows:
    print(row)
    print(f"Inventory ID: {row[0]}")
    print(f"Inventory Name: {row[1]}")
    print(f"Inventory Department: {row[2]}")
    print(f"Inventory Price: {row[3]}")
    print(f"Inventory Quantity: {row[4]}")
    print(f"Inventory Value: {row[5]}")

conn.close()
