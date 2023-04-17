class Inventory():
    def __init__(self, inventoryID, inventoryName, department, inventoryPrice, inventoryQuantity, inventoryValue):
        self.inventoryID = inventoryID
        self.inventoryName = inventoryName
        self.department = department
        self.inventoryPrice = inventoryPrice
        self.inventoryQuantity = inventoryQuantity
        self.inventoryValue = inventoryValue

    def addInventoryItem(self, inventoryID, inventoryName, department, inventoryPrice, inventoryQuantity, inventoryValue):
        inventoryID = input("Enter the inventory ID: ")
        self.inventoryID = inventoryID
        department = input("Enter the department: ")
        self.department = department
        inventoryPrice = float(input("Enter the inventory price: "))
        self.inventoryPrice = inventoryPrice
        inventoryQuantity = float(input("Enter the inventory quantity: "))
        self.inventoryQuantity = inventoryQuantity
        inventoryValue = inventoryPrice * inventoryQuantity
        self.inventoryValue = inventoryValue

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

class User():
    def __init__(self, userID, userName, email, loginPassword, creditCard, address, city, state, country, phone):
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
