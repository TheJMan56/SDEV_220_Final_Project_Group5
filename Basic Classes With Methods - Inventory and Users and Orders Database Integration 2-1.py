import sqlite3
from datetime import date

conn = sqlite3.connect('Inventory_and_Users_and_Orders.db')
curs = conn.cursor()

def obtainInventoryItem(inventoryID):
    sql = 'SELECT * FROM Inventory WHERE inventoryID ='
    inventoryID = str(inventoryID)
    curs.execute(sql + " " + inventoryID)
    row = curs.fetchone()
    return row

class Inventory():
    def __init__(self):
        pass

    def defineInventoryItem(self):
        inventoryID = input("Enter the inventory ID: ")
        self.inventoryID = inventoryID
        inventoryName = input("Enter the inventory Name: ")
        self.inventoryName = inventoryName
        department = input("Enter the department: ")
        self.department = department
        inventoryPrice = float(input("Enter the inventory price: "))
        self.inventoryPrice = inventoryPrice
        inventoryQuantity = float(input("Enter the inventory quantity: "))
        self.inventoryQuantity = inventoryQuantity
        inventoryValue = inventoryPrice * inventoryQuantity
        self.inventoryValue = inventoryValue

    def outputInventoryItem(self):
        print(f"Inventory Item ID: {self.inventoryID}")
        print(f"Inventory Item Name: {self.inventoryName}")
        print(f"Inventory Item Department: {self.department}")
        print(f"Inventory Item Price: {self.inventoryPrice}")
        print(f"Inventory Item Quantity: {self.inventoryQuantity}")
        print(f"Inventory Item Value: {self.inventoryValue}")

    def retrieveInventoryItem(self):
        inventoryID = input("Enter the inventory ID: ")
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

    def alterInventoryItem(self):
        inventoryName = input("Enter the inventory Name: ")
        self.inventoryName = inventoryName
        department = input("Enter the department: ")
        self.department = department
        inventoryPrice = float(input("Enter the inventory price: "))
        self.inventoryPrice = inventoryPrice
        inventoryQuantity = float(input("Enter the inventory quantity: "))
        self.inventoryQuantity = inventoryQuantity
        inventoryValue = inventoryPrice * inventoryQuantity
        self.inventoryValue = inventoryValue

    def alterInventoryQuantity(self):
        inventoryPrice = self.inventoryPrice
        inventoryQuantity = float(input("Enter the inventory quantity: "))
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
        delInventory = 'DELETE FROM Inventory WHERE inventoryID = ?'
        curs.execute(delInventory, self.inventoryID)
        conn.commit()

class User():
    def __init__(self):
        pass

    def defineUser(self):
        userID = input("Enter the user ID: ")
        self.userID = userID
        userName = input("Enter the user name: ")
        self.userName = userName
        email = input("Enter the user email: ")
        self.email = email
        loginPassword = input("Enter the login password: ")
        self.loginPassword = loginPassword
        creditCard = input("Enter the credit card: ")
        self.creditCard = creditCard
        address = input("Enter the address: ")
        self.address = address
        city = input("Enter the city: ")
        self.city = city
        state = input("Enter the state: ")
        self.state = state
        country = input("Enter the country: ")
        self.country = country
        phone = input("Enter the phone: ")
        self.phone = phone

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

    def addUser(self):
        insUser = 'INSERT INTO Users (userID, userName, email, \
        loginPassword, creditCard, address, city, state, country, phone) \
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        curs.execute(insUser, (self.userID, self.userName, self.email, \
                               self.loginPassword, self.creditCard, self.address, \
                               self.city, self.state, self.country, self.phone))
        conn.commit()

    def retrieveUser(self):
        getUser = 'SELECT * FROM Users WHERE userID ='
        userID = input("Enter the user ID: ")
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

    def updateInfo(self):
        userName = input("Enter the user name: ")
        self.userName = userName
        email = input("Enter the user email: ")
        self.email = email
        loginPassword = input("Enter the login password: ")
        self.loginPassword = loginPassword
        creditCard = input("Enter the credit card: ")
        self.creditCard = creditCard
        address = input("Enter the address: ")
        self.address = address
        city = input("Enter the city: ")
        self.city = city
        state = input("Enter the state: ")
        self.state = state
        country = input("Enter the country: ")
        self.country = country
        phone = input("Enter the phone: ")
        self.phone = phone

    def commitUpdatedInfo(self):
        updUser = 'UPDATE Users SET userName = ?, email = ?, loginPassword = ?, \
                   creditCard = ?, address = ?, city = ?, state = ?, \
                   country = ?, phone = ? \
                   WHERE userID = ?'
        curs.execute(updUser, (self.userName, self.email, self.loginPassword, \
                               self.creditCard, self.address, self.city, \
                               self.state, self.country, self.phone, \
                               self.userID))
        conn.commit()

    def resetPassword(self):
        loginPassword = input("Enter the login password: ")
        self.loginPassword = loginPassword

    def commitResetPassword(self):
        updPassword = 'UPDATE Users SET loginPassword = ? WHERE userID = ?'
        curs.execute(updPassword, self.loginPassword)
        conn.commit()

    def deleteUser(self):
        delUser = 'DELETE FROM Users WHERE userID = ?'
        curs.execute(delUser, self.userID)
        conn.commit()

class Order():
    def __init__(self):
        pass

    def startOrder(self):
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
        orderID = input("Enter the order ID: ")
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

    def outputRetrievedOrder(self):
        orderID = input("Enter the order ID: ")
        getOrder = 'SELECT * FROM Orders WHERE orderID ='
        orderID = str(orderID)
        curs.execute(getOrder + " " + orderID)
        orderInfo = curs.fetchone()
        print(f"Order ID: {orderInfo[0]}")
        print(f"User ID: {orderInfo[1]}")
        print(f"Credit Card: {orderInfo[2]}")
        print(f"City: {orderInfo[3]}")
        print(f"State: {orderInfo[4]}")
        print(f"Country: {orderInfo[5]}")
        print(f"Address: {orderInfo[6]}")
        print(f"Items: {orderInfo[7]}")
        print(f"Price Per Item: {orderInfo[8]}")
        print(f"Quantity Per Item: {orderInfo[9]}")
        print(f"Cost Per Item: {orderInfo[10]}")
        print(f"Total Cost: {orderInfo[11]}")
        print(f"Order Date: {orderInfo[12]}")

    def retrieveOrder(self):
        pass
        orderID = input("Enter the order ID: ")
        getOrder = 'SELECT * FROM Orders WHERE orderID ='
        orderID = str(orderID)
        curs.execute(getOrder + " " + orderID)
        orderInfo = curs.fetchone()
        print(f"Order ID: {orderInfo[0]}")
        print(f"User ID: {orderInfo[1]}")
        print(f"Credit Card: {orderInfo[2]}")
        print(f"City: {orderInfo[3]}")
        print(f"State: {orderInfo[4]}")
        print(f"Country: {orderInfo[5]}")
        print(f"Address: {orderInfo[6]}")
        print(f"Items: {orderInfo[7]}")
        print(f"Price Per Item: {orderInfo[8]}")
        print(f"Quantity Per Item: {orderInfo[9]}")
        print(f"Cost Per Item: {orderInfo[10]}")
        print(f"Total Cost: {orderInfo[11]}")
        print(f"Order Date: {orderInfo[12]}")

    def addItems(self):
        items = set()
        pricePerItem = {}
        quantityPerItem = {}
        costPerItem = {}
        originalQuantityPerItem = {}
        originalValuePerItem = {}
        alteredQuantityPerItem = {}
        alteredValuePerItem = {}
        totalCost = 0
        while True:
            inventoryID = input("Enter the inventory ID: ")
            if inventoryID == "":
                break
            inventoryItem = obtainInventoryItem(inventoryID)
            inventoryID = inventoryItem[0]
            inventoryPrice = float(inventoryItem[3])
            inventoryQuantity = float(inventoryItem[4])
            inventoryValue = float(inventoryItem[5])
            orderQuantity = float(input("Enter the order quantity: "))
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

    def addItem(self):
        pass

    def removeItems(self):
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = self.totalCost
        while True:
            inventoryID = input("Enter the inventory ID: ")
            if inventoryID == "":
                break
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

    def removeItem(self):
        pass

    def changeItemQuantities(self):
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = 0
        while True:
            inventoryID = input("Enter the inventory ID: ")
            if inventoryID == "":
                break
            inventoryID = int(inventoryID)
            inventoryPrice = float(pricePerItem[inventoryID])
            inventoryQuantity = originalQuantityPerItem[inventoryID]
            orderQuantity = float(input("Enter the order quantity: "))
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

    def changeItemQuantity(self):
        pass

    def setAddress(self):
        address = input("Enter the order address: ")
        city = input("Enter the order city: ")
        state = input("Enter the order state: ")
        country = input("Enter the order country: ")
        self.address = address
        self.city = city
        self.state = state
        self.country = country

    def setPaymentMethod(self):
        creditCard = input("Enter the order credit card: ")
        self.creditCard = creditCard

    def finilizeOrder(self):
        self.date = str(date.today())
        insOrder = 'INSERT INTO Orders (orderID, userID, creditCard, \
        address, city, state, country, items, pricePerItem, \
        quantityPerItem, costPerItem, totalCost, orderDate) \
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        curs.execute(insOrder, (self.orderID, self.userID, self.creditCard, \
                                self.address, self.city, self.state, \
                                self.country, str(self.items), str(self.pricePerItem), \
                                str(self.quantityPerItem), str(self.costPerItem), \
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

inventoryItem = Inventory()
user = User()
order = Order()

while True:
    choice = input("Enter a function: ")
    if choice == "defineInventoryItem":
        inventoryItem.defineInventoryItem()
    elif choice == "outputInventoryItem":
        inventoryItem.outputInventoryItem()
    elif choice == "retrieveInventoryItem":
        inventoryItem.retrieveInventoryItem()
    elif choice == "addInventoryItem":
        inventoryItem.addInventoryItem()
    elif choice == "alterInventoryItem":
        inventoryItem.alterInventoryItem()
    elif choice == "alterInventoryQuantity":
        inventoryItem.alterInventoryQuantity()
    elif choice == "commitAlteredInventoryItem":
        inventoryItem.commitAlteredInventoryItem()
    elif choice == "defineUser":
        user.defineUser()
    elif choice == "outputUser":
        user.outputUser()
    elif choice == "addUser":
        user.addUser()
    elif choice == "retrieveUser":
        user.retrieveUser()
    elif choice == "updateInfo":
        user.updateInfo()
    elif choice == "commitUpdatedInfo":
        user.commitUpdatedInfo()
    elif choice == "resetPassword":
        user.resetPassword()
    elif choice == "commitResetPassword":
        user.commitResetPassword()
    elif choice == "deleteUser":
        user.deleteUser()
    elif choice == "startOrder":
        order.startOrder()
    elif choice == "outputOrder":
        order.outputOrder()
    elif choice == "outputRetrievedOrder":
        order.outputRetrievedOrder()
    elif choice == "retrieveOrder":
        order.retrieveOrder()
    elif choice == "addItems":
        order.addItems()
    elif choice == "addItem":
        order.addItem()
    elif choice == "removeItems":
        order.removeItems()
    elif choice == "removeItem":
        order.removeItem()
    elif choice == "changeItemQuantities":
        order.changeItemQuantities()
    elif choice == "changeItemQuantity":
        order.changeItemQuantity()
    elif choice == "setPaymentMethod":
        order.setPaymentMethod()
    elif choice == "finilizeOrder":
        order.finilizeOrder()
    elif choice == "deductInventory":
        order.deductInventory()
    elif choice == "":
        break
    else:
        print("Not a valid choice.")

conn.close()
