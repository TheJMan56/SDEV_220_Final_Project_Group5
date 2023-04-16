import sqlite3

conn = sqlite3.connect('Orders.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE Orders
    (orderID INT PRIMARY KEY,
     userID INT,
     creditCard INT,
     city VARCHAR(80),
     state VARCHAR(80),
     country VARCHAR(80),
     address VARCHAR(80),
     items VARCHAR(255),
     pricePerItem VARCHAR(255),
     quantityPerItem VARCHAR(255),
     costPerItem VARCHAR(255),
     totalCost FLOAT,
     orderDate DATE)''')
