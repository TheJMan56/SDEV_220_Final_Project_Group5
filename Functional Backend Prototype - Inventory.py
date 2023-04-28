import sqlite3
from datetime import date

conn = sqlite3.connect('Inventory_and_Users_and_Orders_Updated.db')
curs = conn.cursor()

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def obtainAllInventoryItems():
    curs.execute('SELECT * FROM Inventory')
    rows = curs.fetchall()

    for row in rows:
        print(row)
        print(f"Inventory ID: {row[0]}")
        print(f"Inventory Name: {row[1]}")
        print(f"Inventory Department: {row[2]}")
        print(f"Inventory Price: {row[3]}")
        print(f"Inventory Quantity: {row[4]}")
        print(f"Inventory Value: {row[5]}")

def obtainInventoryItem(inventoryID):
    sql = 'SELECT * FROM Inventory WHERE inventoryID ='
    inventoryID = str(inventoryID)
    curs.execute(sql + " " + inventoryID)
    row = curs.fetchone()
    return row

def deleteInventoryItem(inventoryID):
    sql = 'DELETE FROM Inventory WHERE inventoryID ='
    inventoryID = str(inventoryID)
    curs.execute(sql + " " + inventoryID)
    conn.commit()

def obtainUser(userID):
    sql = 'SELECT * FROM Users WHERE userID ='
    userID = str(userID)
    curs.execute(sql + " " + userID)
    row = curs.fetchone()
    return row

def deleteInventoryItem(userID):
    sql = 'DELETE FROM Users WHERE userID ='
    useID = str(userID)
    curs.execute(sql + " " + userID)
    conn.commit()

def obtainOrder(orderID):
    sql = 'SELECT * FROM Orders WHERE orderID ='
    orderID = str(orderID)
    curs.execute(sql + " " + orderID)
    row = curs.fetchone()
    return row

class Inventory():
    def __init__(self):
        pass

    def newInventoryItem(self, inventoryID, inventoryName, department, inventoryPrice, inventoryQuantity):
        self.inventoryID = inventoryID
        self.inventoryName = inventoryName
        self.department = department
        self.inventoryPrice = inventoryPrice
        self.inventoryQuantity = inventoryQuantity
        inventoryValue = float(inventoryPrice) * float(inventoryQuantity)
        self.inventoryValue = inventoryValue

    def outputInventoryItem(self):
        print(f"Inventory Item ID: {self.inventoryID}")
        print(f"Inventory Item Name: {self.inventoryName}")
        print(f"Inventory Item Department: {self.department}")
        print(f"Inventory Item Price: {self.inventoryPrice}")
        print(f"Inventory Item Quantity: {self.inventoryQuantity}")
        print(f"Inventory Item Value: {self.inventoryValue}")

    def retrieveInventoryItem(self, inventoryID):
        getInventory = 'SELECT * FROM Inventory WHERE inventoryID ='
        inventoryID = str(inventoryID)
        curs.execute(getInventory + " " + inventoryID)
        inventoryItem = curs.fetchone()
        self.inventoryID = inventoryItem[0]
        self.inventoryName = inventoryItem[1]
        self.department = inventoryItem[2]
        self.inventoryPrice = inventoryItem[3]
        self.inventoryQuantity = inventoryItem[4]
        self.inventoryValue = inventoryItem[5]

    def addInventoryItem(self):
        insInventory = 'INSERT INTO Inventory (inventoryID, inventoryName, \
        department, inventoryPrice, inventoryQuantity, inventoryValue) \
        VALUES (?, ?, ?, ?, ?, ?)'
        curs.execute(insInventory, (self.inventoryID, self.inventoryName, \
                                    self.department, self.inventoryPrice, \
                                    self.inventoryQuantity, self.inventoryValue))
        conn.commit()

    def alterInventoryItem(self, inventoryName, department, inventoryPrice, inventoryQuantity):
        self.inventoryName = inventoryName
        self.department = department
        self.inventoryPrice = inventoryPrice
        self.inventoryQuantity = inventoryQuantity
        inventoryValue = inventoryPrice * inventoryQuantity
        self.inventoryValue = inventoryValue

    def alterInventoryQuantity(self, inventoryQuantity):
        inventoryPrice = self.inventoryPrice
        self.inventoryQuantity = inventoryQuantity
        inventoryValue = inventoryPrice * inventoryQuantity
        self.inventoryValue = inventoryValue

    def commitAlteredInventoryItem(self):
        updInventory = 'UPDATE Inventory SET inventoryName = ?, \
                        department = ?, inventoryPrice = ?, inventoryQuantity = ?, \
                        inventoryValue = ? \
                        WHERE inventoryID = ?'
        curs.execute(updInventory, (self.inventoryName, self.department, \
                                    self.inventoryPrice, self.inventoryQuantity, \
                                    self.inventoryValue, self.inventoryID))
        conn.commit()

    def deleteInventoryItem(self):
        delInventory = 'DELETE FROM Inventory WHERE inventoryID ='
        inventoryID = str(self.inventoryID)
        curs.execute(delInventory + " " + inventoryID)
        conn.commit()
