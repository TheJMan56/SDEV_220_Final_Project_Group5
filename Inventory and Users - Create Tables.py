import sqlite3

conn = sqlite3.connect('Inventory_and_Users.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE Inventory
    (inventoryID INT PRIMARY KEY,
     inventoryName VARCHAR(80),
     department VARCHAR(80),
     inventoryPrice FLOAT,
     inventoryQuantity FLOAT,
     inventoryValue FLOAT)''')

curs.execute('''CREATE TABLE Users
    (userID INT PRIMARY KEY,
     userName VARCHAR(80),
     email VARCHAR(80),
     loginPassword VARCHAR(40),
     creditCard INT,
     city VARCHAR(80),
     state VARCHAR(80),
     country VARCHAR(80),
     address VARCHAR(80),
     phone INT)''')
