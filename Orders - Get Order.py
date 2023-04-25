import sqlite3

conn = sqlite3.connect('Inventory_and_Users_and_Orders.db')
curs = conn.cursor()

curs.execute('SELECT * FROM Orders')
rows = curs.fetchall()

print(rows)

for row in rows:
    print(row)
    print(f"Order ID: {row[0]}")
    print(f"User ID: {row[1]}")
    print(f"Credit Card: {row[2]}")
    print(f"City: {row[3]}")
    print(f"State: {row[4]}")
    print(f"Country: {row[5]}")
    print(f"Address: {row[6]}")
    print(f"Items: {row[7]}")
    print(f"Price Per Item: {row[8]}")
    print(f"Quantity Per Item: {row[9]}")
    print(f"Cost Per Item: {row[10]}")
    print(f"Total Cost: {row[11]}")
    print(f"Order Date: {row[12]}")

conn.close()
