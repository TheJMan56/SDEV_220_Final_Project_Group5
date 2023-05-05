from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from datetime import date

conn = sqlite3.connect('Inventory_and_Users_and_Orders_Updated.db', check_same_thread=False)
curs = conn.cursor()

# Create your views here.

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

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

class User():
    def __init__(self):
        pass

    def newUser(self, userID, userName, email, loginPassword, creditCard, address, city, state, country, phone):
        self.userID = userID
        self.userName = userName
        self.email = email
        self.loginPassword = loginPassword
        self.creditCard = creditCard
        self.address = address
        self.city = city
        self.state = state
        self.country = country
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

    def updateInfo(self, userName, email, loginPassword, creditCard, address, city, state, country, phone):
        self.userName = userName
        self.email = email
        self.loginPassword = loginPassword
        self.creditCard = creditCard
        self.address = address
        self.city = city
        self.state = state
        self.country = country
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

    def resetPassword(self, loginPassword):
        self.loginPassword = loginPassword

    def commitResetPassword(self):
        updPassword = 'UPDATE Users SET loginPassword = ? WHERE userID = ?'
        curs.execute(updPassword, (self.loginPassword, self.userID))
        conn.commit()

    def deleteUser(self):
        delUser = 'DELETE FROM Users WHERE userID ='
        userID = str(self.userID)
        curs.execute(delUser + " " + userID)
        conn.commit()

    def loginUser(self, userID, inputPassword):
        getUser = 'SELECT * FROM Users WHERE userID ='
        userID = str(userID)
        curs.execute(getUser + " " + userID)
        userData = curs.fetchone()

        correctPassword = userData[3]
        
        if inputPassword == correctPassword:
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
        else:
            print("Incorrect password.")

class Order():
    def __init__(self):
        pass

    def newOrder(self, orderID, user):
        items = set()
        pricePerItem = {}
        quantityPerItem = {}
        costPerItem = {}
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
        self.orderID = orderInfo[0]
        self.userID = orderInfo[1]
        self.creditCard = orderInfo[2]
        self.city = orderInfo[3]
        self.state = orderInfo[4]
        self.country = orderInfo[5]
        self.address = orderInfo[6]
        self.items = orderInfo[7]
        self.pricePerItem = orderInfo[8]
        self.quantityPerItem = orderInfo[9]
        self.costPerItem = orderInfo[10]
        self.originalQuantityPerItem = orderInfo[11]
        self.originalValuePerItem = orderInfo[12]
        self.alteredQuantityPerItem = orderInfo[13]
        self.alteredValuePerItem = orderInfo[14]
        self.totalCost = orderInfo[15]
        self.date = orderInfo[16]

    def retrievedOrder(self, orderID, userID, creditCard, city, state, country, address, items, pricePerItem, quantityPerItem, costPerItem, originalQuantityPerItem, originalValuePerItem, alteredQuantityPerItem, alteredValuePerItem, totalCost, date):
        self.orderID = orderID
        self.userID = userID
        self.creditCard = creditCard
        self.city = city
        self.state = state
        self.country = country
        self.address = address
        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost
        self.date = date

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

    def finalizeOrder(self):
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

def inventoryMenu(request):
    return render(request, "inventoryMenu.html")

def newInventoryItem(request):
    inventoryID = int(request.GET["inventoryID"])
    inventoryName = request.GET["inventoryName"]
    department = request.GET["department"]
    inventoryPrice = float(request.GET["inventoryPrice"])
    inventoryQuantity = float(request.GET["inventoryQuantity"])
    
    global inventoryItem
    inventoryItem = Inventory()
    inventoryItem.newInventoryItem(inventoryID, inventoryName, department, inventoryPrice, inventoryQuantity)

    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def outputInventoryItem(request):
    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def retrieveInventoryItem(request):
    inventoryID = request.GET["inventoryID"]

    getInventory = 'SELECT * FROM Inventory WHERE inventoryID ='
    inventoryID = str(inventoryID)
    curs.execute(getInventory + " " + inventoryID)
    inventoryQuery = curs.fetchone()

    inventoryID = inventoryQuery[0]
    inventoryName = inventoryQuery[1]
    department = inventoryQuery[2]
    inventoryPrice = inventoryQuery[3]
    inventoryQuantity = inventoryQuery[4]
    inventoryValue = inventoryQuery[5]

    global inventoryItem
    inventoryItem = Inventory()
    inventoryItem.newInventoryItem(inventoryID, inventoryName, department, inventoryPrice, inventoryQuantity)

    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def addCurrentInventoryItem(request):
    insInventory = 'INSERT INTO Inventory (inventoryID, inventoryName, \
        department, inventoryPrice, inventoryQuantity, inventoryValue) \
        VALUES (?, ?, ?, ?, ?, ?)'
    curs.execute(insInventory, (inventoryItem.inventoryID, inventoryItem.inventoryName, \
                                inventoryItem.department, inventoryItem.inventoryPrice, \
                                inventoryItem.inventoryQuantity, inventoryItem.inventoryValue))
    conn.commit()
    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def addNewInventoryItem(request):
    inventoryID = int(request.GET["inventoryID"])
    inventoryName = request.GET["inventoryName"]
    department = request.GET["department"]
    inventoryPrice = float(request.GET["inventoryPrice"])
    inventoryQuantity = float(request.GET["inventoryQuantity"])
    
    global inventoryItem
    inventoryItem = Inventory()
    inventoryItem.newInventoryItem(inventoryID, inventoryName, department, inventoryPrice, inventoryQuantity)

    insInventory = 'INSERT INTO Inventory (inventoryID, inventoryName, \
                    department, inventoryPrice, inventoryQuantity, inventoryValue) \
                    VALUES (?, ?, ?, ?, ?, ?)'
    curs.execute(insInventory, (inventoryItem.inventoryID, inventoryItem.inventoryName, \
                                inventoryItem.department, inventoryItem.inventoryPrice, \
                                inventoryItem.inventoryQuantity, inventoryItem.inventoryValue))
    conn.commit()
    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def alterInventoryItem(request):
    inventoryName = request.GET["inventoryName"]
    department = request.GET["department"]
    inventoryPrice = float(request.GET["inventoryPrice"])
    inventoryQuantity = float(request.GET["inventoryQuantity"])

    inventoryItem.alterInventoryItem(inventoryName, department, inventoryPrice, inventoryQuantity)
    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def alterInventoryQuantity(request):
    inventoryQuantity = float(request.GET["inventoryQuantity"])

    inventoryItem.alterInventoryQuantity(inventoryQuantity)
    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def commitAlteredInventoryItem(request):
    updInventory = 'UPDATE Inventory SET inventoryName = ?, \
                    department = ?, inventoryPrice = ?, inventoryQuantity = ?, \
                    inventoryValue = ? \
                    WHERE inventoryID = ?'
    curs.execute(updInventory, (inventoryItem.inventoryName, inventoryItem.department, \
                                inventoryItem.inventoryPrice, inventoryItem.inventoryQuantity, \
                                inventoryItem.inventoryValue, inventoryItem.inventoryID))
    conn.commit()

def deleteCurrentInventoryItem(request):
    delInventory = 'DELETE FROM Inventory WHERE inventoryID ='
    inventoryID = str(inventoryItem.inventoryID)
    curs.execute(delInventory + " " + inventoryID)
    conn.commit()
    return HttpResponse("<html><body><p>Inventory Item Deleted</p></body></html>")

def deleteSelectedInventoryItem(request):
    delInventory = 'DELETE FROM Inventory WHERE inventoryID ='
    inventoryID = str(request.GET["inventoryID"])
    curs.execute(delInventory + " " + inventoryID)
    conn.commit()
    return HttpResponse("<html><body><p>Inventory Item Deleted</p></body></html>")

def userMenu(request):
    return render(request, "userMenu.html")

def newUser(request):
    userID = int(request.GET["userID"])
    userName = request.GET["userName"]
    email = request.GET["email"]
    loginPassword = request.GET["loginPassword"]
    creditCard = request.GET["creditCard"]
    city = request.GET["city"]
    state = request.GET["state"]
    country = request.GET["country"]
    address = request.GET["address"]
    phone = request.GET["phone"]
    
    global user
    user = User()
    user.newUser(userID, userName, email, loginPassword, creditCard, address, city, state, country, phone)

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def outputUser(request):
    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def addCurrentUser(request):
    insUser = 'INSERT INTO Users (userID, userName, email, \
              loginPassword, creditCard, address, city, state, country, phone) \
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    curs.execute(insUser, (user.userID, user.userName, user.email, \
                           user.loginPassword, user.creditCard, user.address, \
                           user.city, user.state, user.country, user.phone))
    conn.commit()

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def addNewUser(request):
    userID = int(request.GET["userID"])
    userName = request.GET["userName"]
    email = request.GET["email"]
    loginPassword = request.GET["loginPassword"]
    creditCard = request.GET["creditCard"]
    city = request.GET["city"]
    state = request.GET["state"]
    country = request.GET["country"]
    address = request.GET["address"]
    phone = request.GET["phone"]
    
    global user
    user = User()
    user.newUser(userID, userName, email, loginPassword, creditCard, address, city, state, country, phone)

    insUser = 'INSERT INTO Users (userID, userName, email, \
              loginPassword, creditCard, address, city, state, country, phone) \
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    curs.execute(insUser, (user.userID, user.userName, user.email, \
                           user.loginPassword, user.creditCard, user.address, \
                           user.city, user.state, user.country, user.phone))
    conn.commit()

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def retrieveUser(request):
    userID = request.GET["userID"]

    getUser = 'SELECT * FROM Users WHERE userID ='
    userID = str(userID)
    curs.execute(getUser + " " + userID)
    userData = curs.fetchone()

    userID = userData[0]
    userName = userData[1]
    email = userData[2]
    loginPassword = userData[3]
    creditCard = userData[4]
    city = userData[5]
    state = userData[6]
    country = userData[7]
    address = userData[8]
    phone = userData[9]

    global user
    user = User()
    user.newUser(userID, userName, email, loginPassword, creditCard, address, city, state, country, phone)

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def updateUserInfo(request):
    userName = request.GET["userName"]
    email = request.GET["email"]
    loginPassword = request.GET["loginPassword"]
    creditCard = request.GET["creditCard"]
    city = request.GET["city"]
    state = request.GET["state"]
    country = request.GET["country"]
    address = request.GET["address"]
    phone = request.GET["phone"]

    user.updateInfo(userName, email, loginPassword, creditCard, address, city, state, country, phone)

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def commitUpdatedInfo(request):
    updUser = 'UPDATE Users SET userName = ?, email = ?, loginPassword = ?, \
               creditCard = ?, address = ?, city = ?, state = ?, \
               country = ?, phone = ? \
               WHERE userID = ?'
    curs.execute(updUser, (user.userName, user.email, user.loginPassword, \
                           user.creditCard, user.address, user.city, \
                           user.state, user.country, user.phone, \
                           user.userID))
    conn.commit()

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def resetPassword(request):
    loginPassword = request.GET["loginPassword"]

    user.resetPassword(loginPassword)

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def commitResetPassword(request):
    updPassword = 'UPDATE Users SET loginPassword = ? WHERE userID = ?'
    curs.execute(updPassword, (user.loginPassword, user.userID))
    conn.commit()

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def deleteCurrentUser(request):
    userID = user.userID
    delUser = 'DELETE FROM Users WHERE userID ='
    userID = str(userID)
    curs.execute(delUser + " " + userID)    
    conn.commit()

    return HttpResponse("<html><body><p>User Deleted</p></body></html>")

def deleteSelectedUser(request):
    userID = request.GET["userID"]
    delUser = 'DELETE FROM Users WHERE userID ='
    userID = str(userID)
    curs.execute(delUser + " " + userID)    
    conn.commit()

    return HttpResponse("<html><body><p>User Deleted</p></body></html>")

def loginUser(request):
    userID = request.GET["userID"]
    loginPassword = request.GET["loginPassword"]
    getUser = 'SELECT * FROM Users WHERE userID ='
    userID = str(userID)
    curs.execute(getUser + " " + userID)
    userData = curs.fetchone()

    correctPassword = userData[3]
        
    if loginPassword == correctPassword:
        userID = userData[0]
        userName = userData[1]
        email = userData[2]
        loginPassword = userData[3]
        creditCard = userData[4]
        city = userData[5]
        state = userData[6]
        country = userData[7]
        address = userData[8]
        phone = userData[9]
        
        global user
        user = User()
        user.newUser(userID, userName, email, loginPassword, creditCard, address, city, state, country, phone)
        return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})
    else:
        return HttpResponse("<html><body><p>Incorrect Password</p></body></html>")

def orderMenu(request):
    return render(request, "orderMenu.html")

def newOrder(request):
    orderID = request.GET["orderID"]

    global order
    order = Order()
    order.newOrder(orderID, user)

    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def outputOrder(request):
    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def retrieveOrder(request):
    orderID = request.GET["orderID"]
    orderID = str(orderID)
    getOrder = 'SELECT * FROM Orders WHERE orderID ='
    curs.execute(getOrder + " " + orderID)
    orderInfo = curs.fetchone()

    orderID = orderInfo[0]
    userID = orderInfo[1]
    creditCard = orderInfo[2]
    city = orderInfo[3]
    state = orderInfo[4]
    country = orderInfo[5]
    address = orderInfo[6]
    items = orderInfo[7]
    pricePerItem = orderInfo[8]
    quantityPerItem = orderInfo[9]
    costPerItem = orderInfo[10]
    originalQuantityPerItem = orderInfo[11]
    originalValuePerItem = orderInfo[12]
    alteredQuantityPerItem = orderInfo[13]
    alteredValuePerItem = orderInfo[14]
    totalCost = orderInfo[15]
    date = orderInfo[16]

    global order
    order = Order()
    order.retrievedOrder(orderID, userID, creditCard, city, state, country, address, items, pricePerItem, quantityPerItem, costPerItem, originalQuantityPerItem, originalValuePerItem, alteredQuantityPerItem, alteredValuePerItem, totalCost, date)

    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": order.date})

def setAddress(request):
    city = request.GET["city"]
    state = request.GET["state"]
    country = request.GET["country"]
    address = request.GET["address"]

    order.setAddress(address, city, state, country)
    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def setPaymentMethod(request):
    creditCard = request.GET["creditCard"]

    order.setPaymentMethod(creditCard)
    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def addItem(request):
    orderQuantity = float(request.GET["orderQuantity"])

    order.addItem(inventoryItem, orderQuantity)
    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def addItemWithID(request):
    inventoryID = int(request.GET["inventoryID"])
    orderQuantity = float(request.GET["orderQuantity"])

    items = set(order.items)
    pricePerItem = dict(order.pricePerItem)
    quantityPerItem = dict(order.quantityPerItem)
    costPerItem = dict(order.costPerItem)
    originalQuantityPerItem = dict(order.originalQuantityPerItem)
    originalValuePerItem = dict(order.originalValuePerItem)
    alteredQuantityPerItem = dict(order.alteredQuantityPerItem)
    alteredValuePerItem = dict(order.alteredValuePerItem)
    totalCost = float(order.totalCost)

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
    
    order.items = items
    order.pricePerItem = pricePerItem
    order.quantityPerItem = quantityPerItem
    order.costPerItem = costPerItem
    order.originalQuantityPerItem = originalQuantityPerItem
    order.originalValuePerItem = originalValuePerItem
    order.alteredQuantityPerItem = alteredQuantityPerItem
    order.alteredValuePerItem = alteredValuePerItem
    order.totalCost = totalCost

    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def removeItem(request):
    order.removeItem(inventoryItem)

    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def removeItemWithID(request):
    inventoryID = request.GET["inventoryID"]
    order.removeItemWithID(inventoryID)

    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def changeItemQuantity(request):
    orderQuantity = float(request.GET["orderQuantity"])
    order.changeItemQuantity(inventoryItem, orderQuantity)

    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def changeItemQuantityWithID(request):
    inventoryID = int(request.GET["inventoryID"])
    orderQuantity = float(request.GET["orderQuantity"])
    order.changeItemQuantityWithID(inventoryID, orderQuantity)

    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def finalizeOrder(request):
    order.date = str(date.today())
    insOrder = 'INSERT INTO Orders (orderID, userID, creditCard, \
                address, city, state, country, items, pricePerItem, \
                quantityPerItem, costPerItem, originalQuantityPerItem, \
                originalValuePerItem, alteredQuantityPerItem, alteredValuePerItem, \
                totalCost, orderDate) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    curs.execute(insOrder, (order.orderID, order.userID, order.creditCard, \
                            order.address, order.city, order.state, \
                            order.country, str(order.items), str(order.pricePerItem), \
                            str(order.quantityPerItem), str(order.costPerItem), \
                            str(order.originalQuantityPerItem), str(order.originalValuePerItem), \
                            str(order.alteredQuantityPerItem), str(order.alteredValuePerItem), \
                            order.totalCost, order.date))
    conn.commit()

    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": order.date})

def deductInventory(request):
    items = order.items
    items = set(items)
    alteredQuantityPerItem = order.alteredQuantityPerItem
    alteredQuantityPerItem = dict(alteredQuantityPerItem)
    alteredValuePerItem = order.alteredValuePerItem
    alteredValuePerItem = dict(alteredValuePerItem)
    updQuantity = 'UPDATE Inventory SET inventoryQuantity = ?, \
                  inventoryValue = ? WHERE inventoryID = ?'
    for inventoryID in items:
        inventoryQuantity = alteredQuantityPerItem[inventoryID]
        inventoryValue = alteredValuePerItem[inventoryID]
        curs.execute(updQuantity, (inventoryQuantity, inventoryValue, inventoryID))
        conn.commit()
