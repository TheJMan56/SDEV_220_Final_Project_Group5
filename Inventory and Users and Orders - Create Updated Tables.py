import sqlite3

conn = sqlite3.connect('Inventory_and_Users_and_Orders_Updated.db')
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
     creditCard CHAR(16),
     city VARCHAR(80),
     state VARCHAR(80),
     country VARCHAR(80),
     address VARCHAR(80),
     phone CHAR(10))''')

curs.execute('''CREATE TABLE Orders
    (orderID INT PRIMARY KEY,
     userID INT,
     creditCard CHAR(16),
     city VARCHAR(80),
     state VARCHAR(80),
     country VARCHAR(80),
     address VARCHAR(80),
     items VARCHAR(255),
     pricePerItem VARCHAR(255),
     quantityPerItem VARCHAR(255),
     costPerItem VARCHAR(255),
     originalQuantityPerItem VARCHAR(255),
     originalValuePerItem VARCHAR(255),
     alteredQuantityPerItem VARCHAR(255),
     alteredValuePerItem VARCHAR(255),
     totalCost FLOAT,
     orderDate DATE)''')

conn.close()
