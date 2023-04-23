import sqlite3

conn = sqlite3.connect('Inventory_and_Users_and_Orders.db')
curs = conn.cursor()

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
        self.address = userData[5]
        self.city = userData[6]
        self.state = userData[7]
        self.country = userData[8]
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

    def makeOrder(self):
        pass

class Order():
    def __init__(self):
        pass

    def startOrder(self):
        items = {}
        pricePerItem = {}
        quantityPerItem = {}
        costPerItem = {}
        totalPerItem = {}
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
        print(f"Total Cost: {self.totalCost}")

    def retrieveOrder(self):
        pass

    def addItem(self):
        pass

    def removeItem(self):
        pass

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
        pass

    def deductInventory(self):
        pass

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
    elif choice == "makeOrder":
        user.makeOrder()
    elif choice == "startOrder":
        order.startOrder()
    elif choice == "outputOrder":
        order.outputOrder()
    elif choice == "retrieveOrder":
        order.retrieveOrder()
    elif choice == "addItem":
        order.addItem()
    elif choice == "removeItem":
        order.removeItem()
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
