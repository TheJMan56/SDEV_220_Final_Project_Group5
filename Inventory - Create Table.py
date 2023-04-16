import sqlite3

conn = sqlite3.connect('Inventory.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE Inventory
    (inventoryID INT PRIMARY KEY,
     inventoryName VARCHAR(80),
     department VARCHAR(80),
     inventoryPrice FLOAT,
     inventoryQuantity FLOAT,
     inventoryValue FLOAT)''')
