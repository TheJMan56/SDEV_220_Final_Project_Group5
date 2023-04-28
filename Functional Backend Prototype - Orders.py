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

def obtainAllUsers():
    curs.execute('SELECT * FROM Users')
    rows = curs.fetchall()

    for row in rows:
        print(f"User ID: {row[0]}")
        print(f"User Name: {row[1]}")
        print(f"User Email: {row[2]}")
        print(f"User Password: {row[3]}")
        print(f"User Credit Card: {row[4]}")
        print(f"User City: {row[5]}")
        print(f"User State: {row[6]}")
        print(f"User Country: {row[7]}")
        print(f"User Address: {row[8]}")
        print(f"User Phone: {row[9]}")

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

def obtainAllOrders():
    curs.execute('SELECT * FROM Orders')
    rows = curs.fetchall()

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
        print(f"Original Quantity Per Item : {row[11]}"
        print(f"Original Value Per Item : {row[12]}"
        print(f"Altered Quantity Per Item : {row[13]}"
        print(f"Altered Value Per Item : {row[14]}"
        print(f"Total Cost: {row[15]}")
        print(f"Order Date: {row[16]}")

def obtainOrder(orderID):
    sql = 'SELECT * FROM Orders WHERE orderID ='
    orderID = str(orderID)
    curs.execute(sql + " " + orderID)
    row = curs.fetchone()
    return row

class Inventory():
    def __init__(self):
        pass

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

    def outputInventoryItem(self):
        print(f"Inventory Item ID: {self.inventoryID}")
        print(f"Inventory Item Name: {self.inventoryName}")
        print(f"Inventory Item Department: {self.department}")
        print(f"Inventory Item Price: {self.inventoryPrice}")
        print(f"Inventory Item Quantity: {self.inventoryQuantity}")
        print(f"Inventory Item Value: {self.inventoryValue}")

class User():
    def __init__(self):
        pass

    def retrieveUser(self, userID):
        getUser = 'SELECT * FROM Users WHERE userID ='
        userID = str(userID)
        curs.execute(getUser + " " + userID)
        userData = curs.fetchone()
        self.userID = userData[0]
        self.userName = userData[1]
        self.email = userData[2]
        self.loginPassword = userData[3]
        self.creditCard = userData[4]
        self.city = userData[5]
        self.state = userData[6]
        self.country = userData[7]
        self.address = userData[8]
        self.phone = userData[9]

    def outputUser(self):
        print(f"User ID: {self.userID}")
        print(f"User Name: {self.userName}")
        print(f"User Email: {self.email}")
        print(f"User Passowrd: {self.loginPassword}")
        print(f"User Credit Card: {self.creditCard}")
        print(f"User Address: {self.address}")
        print(f"User City: {self.city}")
        print(f"User State: {self.state}")
        print(f"User Country: {self.country}")
        print(f"Phone: {self.phone}")

class Order():
    def __init__(self):
        pass

    def newOrder(self, orderID, user):
        items = set()
        pricePerItem = {}
        quantityPerItem = {}
        costPerItem = {}
        totalPerItem = {}
        originalQuantityPerItem = {}
        originalValuePerItem = {}
        alteredQuantityPerItem = {}
        alteredValuePerItem = {}
        totalCost = 0
        self.orderID = orderID
        self.userID = user.userID
        self.creditCard = user.creditCard
        self.address = user.address
        self.city = user.city
        self.state = user.state
        self.country = user.country
        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost

    def outputOrder(self):
        print(f"Order ID: {self.orderID}")
        print(f"User ID: {self.userID}")
        print(f"Credit Card: {self.creditCard}")
        print(f"Address: {self.address}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Country: {self.country}")
        print(f"Items: {self.items}")
        print(f"Price Per Item: {self.pricePerItem}")
        print(f"Quantity Per Item: {self.quantityPerItem}")
        print(f"Cost Per Item: {self.costPerItem}")
        print(f"Original Quantity Per Item: {self.originalQuantityPerItem}")
        print(f"Original Value Per Item: {self.originalValuePerItem}")
        print(f"Altered Quantity Per Item: {self.alteredQuantityPerItem}")
        print(f"Altered Value Per Item: {self.alteredValuePerItem}")
        print(f"Total Cost: {self.totalCost}")

    def retrieveOrder(self, orderID):
        orderID = str(orderID)
        getOrder = 'SELECT * FROM Orders WHERE orderID ='
        curs.execute(getOrder + " " + orderID)
        orderInfo = curs.fetchone()
        self.userID = orderInfo[0]
        self.creditCard = orderInfo[1]
        self.address = orderInfo[2]
        self.city = orderInfo[3]
        self.state = orderInfo[4]
        self.country = orderInfo[5]
        self.items = orderInfo[6]
        self.pricePerItem = orderInfo[7]
        self.quantityPerItem = orderInfo[8]
        self.costPerItem = orderInfo[9]
        self.originalQuantityPerItem = orderInfo[10]
        self.originalValuePerItem = orderInfo[11]
        self.alteredQuantityPerItem = orderInfo[12]
        self.alteredValuePerItem = orderInfo[13]
        self.totalCost = orderInfo[14]
        self.date = orderInfo[15]

    def addItemWithID(self, inventoryID, orderQuantity):
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = float(self.totalCost)

        inventoryItem = obtainInventoryItem(inventoryID)
        inventoryID = inventoryItem[0]
        inventoryPrice = float(inventoryItem[3])
        inventoryQuantity = float(inventoryItem[4])
        inventoryValue = float(inventoryItem[5])
        alteredInventoryQuantity = inventoryQuantity - orderQuantity
        alteredInventoryValue = inventoryPrice * alteredInventoryQuantity
        orderPrice = inventoryPrice * orderQuantity
        totalCost += orderPrice
        items.add(inventoryID)
        pricePerItem[inventoryID] = inventoryPrice
        quantityPerItem[inventoryID] = orderQuantity
        costPerItem[inventoryID] = orderPrice
        originalQuantityPerItem[inventoryID] = inventoryQuantity
        alteredQuantityPerItem[inventoryID]= alteredInventoryQuantity
        originalValuePerItem[inventoryID] = inventoryValue
        alteredValuePerItem[inventoryID] = alteredInventoryValue
        
        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost

    def addItem(self, inventoryItem, orderQuantity):
        inventoryID = inventoryItem.inventoryID
        inventoryQuantity = inventoryItem.inventoryQuantity
        inventoryPrice = inventoryItem.inventoryPrice
        inventoryValue = inventoryItem.inventoryValue
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = 0

        alteredInventoryQuantity = inventoryQuantity - orderQuantity
        alteredInventoryValue = inventoryPrice * alteredInventoryQuantity
        orderPrice = inventoryPrice * orderQuantity
        
        items.add(inventoryID)
        pricePerItem[inventoryID] = inventoryPrice
        quantityPerItem[inventoryID] = orderQuantity
        costPerItem[inventoryID] = orderPrice
        originalQuantityPerItem[inventoryID] = inventoryItem.inventoryQuantity
        alteredQuantityPerItem[inventoryID]= alteredInventoryQuantity
        originalValuePerItem[inventoryID] = inventoryItem.inventoryValue
        alteredValuePerItem[inventoryID] = alteredInventoryValue

        for key in costPerItem:
            totalCost += costPerItem[key]

        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost

    def removeItemWithID(self, inventoryID):
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = self.totalCost

        inventoryID = int(inventoryID)
        totalCost = totalCost - costPerItem[inventoryID]
        items.remove(inventoryID)
        del pricePerItem[inventoryID]
        del quantityPerItem[inventoryID]
        del costPerItem[inventoryID]
        del originalQuantityPerItem[inventoryID]
        del originalValuePerItem[inventoryID]
        del alteredQuantityPerItem[inventoryID]
        del alteredValuePerItem[inventoryID]

        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost

    def removeItem(self, iventoryItem):
        inventoryID = inventoryItem.inventoryID
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = self.totalCost
        
        inventoryID = int(inventoryID)
        totalCost = totalCost - costPerItem[inventoryID]
        items.remove(inventoryID)
        del pricePerItem[inventoryID]
        del quantityPerItem[inventoryID]
        del costPerItem[inventoryID]
        del originalQuantityPerItem[inventoryID]
        del originalValuePerItem[inventoryID]
        del alteredQuantityPerItem[inventoryID]
        del alteredValuePerItem[inventoryID]
        
        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost

    def changeItemQuantityWithID(self, inventoryID, orderQuantity):
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = 0

        inventoryID = int(inventoryID)
        inventoryPrice = float(pricePerItem[inventoryID])
        inventoryQuantity = originalQuantityPerItem[inventoryID]
        orderQuantity = float(orderQuantity)
        orderPrice = inventoryPrice * orderQuantity
        alteredInventoryQuantity = inventoryQuantity - orderQuantity
        alteredInventoryValue = inventoryPrice * alteredInventoryQuantity
        quantityPerItem[inventoryID] = orderQuantity
        costPerItem[inventoryID] = orderPrice
        alteredQuantityPerItem[inventoryID] = alteredInventoryQuantity
        alteredValuePerItem[inventoryID] = alteredInventoryValue

        for key in costPerItem:
            totalCost += costPerItem[key]

        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost

    def changeItemQuantity(self, inventoryItem, orderQuantity):
        inventoryID = inventoryItem.inventoryID
        inventoryQuantity = inventoryItem.inventoryQuantity
        inventoryPrice = inventoryItem.inventoryPrice
        inventoryValue = inventoryItem.inventoryValue
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = 0

        orderQuantity = float(orderQuantity)
        alteredInventoryQuantity = inventoryQuantity - orderQuantity
        alteredInventoryValue = inventoryPrice * alteredInventoryQuantity
        orderPrice = inventoryPrice * orderQuantity
        
        pricePerItem[inventoryID] = inventoryPrice
        quantityPerItem[inventoryID] = orderQuantity
        costPerItem[inventoryID] = orderPrice
        originalQuantityPerItem[inventoryID] = inventoryItem.inventoryQuantity
        alteredQuantityPerItem[inventoryID]= alteredInventoryQuantity
        originalValuePerItem[inventoryID] = inventoryItem.inventoryValue
        alteredValuePerItem[inventoryID] = alteredInventoryValue

        for key in costPerItem:
            totalCost += costPerItem[key]

        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost

    def setAddress(self, address, city, state, country):
        self.address = address
        self.city = city
        self.state = state
        self.country = country

    def setPaymentMethod(self, creditCard):
        self.creditCard = creditCard

    def finilizeOrder(self):
        self.date = str(date.today())
        insOrder = 'INSERT INTO Orders (orderID, userID, creditCard, \
        address, city, state, country, items, pricePerItem, \
        quantityPerItem, costPerItem, originalQuantityPerItem, \
        originalValuePerItem, alteredQuantityPerItem, alteredValuePerItem, \
        totalCost, orderDate) \
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        curs.execute(insOrder, (self.orderID, self.userID, self.creditCard, \
                                self.address, self.city, self.state, \
                                self.country, str(self.items), str(self.pricePerItem), \
                                str(self.quantityPerItem), str(self.costPerItem), \
                                str(self.originalQuantityPerItem), str(self.originalValuePerItem), \
                                str(self.alteredQuantityPerItem), str(self.alteredValuePerItem), \
                                self.totalCost, self.date))
        conn.commit()

    def deductInventory(self):
        items = set(self.items)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        updQuantity = 'UPDATE Inventory SET inventoryQuantity = ?, \
                      inventoryValue = ? WHERE inventoryID = ?'
        for inventoryID in items:
            inventoryQuantity = alteredQuantityPerItem[inventoryID]
            inventoryValue = alteredValuePerItem[inventoryID]
            curs.execute(updQuantity, (inventoryQuantity, inventoryValue, inventoryID))
            conn.commit()
