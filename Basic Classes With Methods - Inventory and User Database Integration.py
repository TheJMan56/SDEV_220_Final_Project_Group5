import sqlite3

conn = sqlite3.connect('Inventory_and_Users.db')
curs = conn.cursor()

class Inventory():
    def __init__(self):
        pass

    def addInventoryItem(self):
        insInventory = 'INSERT INTO Inventory (inventoryID, inventoryName, \
        department, inventoryPrice, inventoryQuantity, inventoryValue) \
        VALUES (?, ?, ?, ?, ?, ?)'
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
        curs.execute(insInventory, (self.inventoryID, self.inventoryName, \
                                    self.department, self.inventoryPrice, \
                                    self.inventoryQuantity, self.inventoryValue))
        conn.commit()

class User():
    def __init__(self):
        pass

    def addUser(self):
        insUser = 'INSERT INTO Users (userID, userName, email, \
        loginPassword, creditCard, address, city, state, country, phone) \
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
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
        curs.execute(insUser, (self.userID, self.userName, self.email, \
                               self.loginPassword, self.creditCard, self.address, \
                               self.city, self.state, self.country, self.phone))
        conn.commit()

class Order():
    def __init__(self, orderID, userID, creditCard, address, city, state, country, items, pricePerItem, quantityPerItem, costPerItem, totalCost, orderDate):
        self.orderID = orderID
        self.userID = userID
        self.creditCard = creditCard
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.totalCost = totalCost
        self.orderDate = orderDate

while True:
    sentinel = input("Continue")
    if sentinel == "":
        break
    inventoryItem = Inventory()
    inventoryItem.addInventoryItem()

while True:
    sentinel = input("Continue")
    if sentinel == "":
        break
    user = User()
    user.addUser()

conn.close()
