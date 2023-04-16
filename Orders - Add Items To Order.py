import sqlite3

conn = sqlite3.connect('Inventory.db')
curs = conn.cursor()

def obtainInventoryItem(inventoryID):
    sql = 'SELECT * FROM Inventory WHERE inventoryID ='
    inventoryID = str(inventoryID)
    curs.execute(sql + " " + inventoryID)
    row = curs.fetchone()
    return row

inventoryItems = []
pricePerItem = {}
quantityPerItem = {}
totalPerItem = {}
orderTotal = 0

while True:
    inventoryID = input("Enter the inventory ID: ")
    if inventoryID == "":
        break
    inventoryItem = obtainInventoryItem(inventoryID)
    inventoryID = inventoryItem[0]
    inventoryPrice = float(inventoryItem[3])
    inventoryQuantity = float(inventoryItem[4])
    orderQuantity = float(input("Enter the order quantity: "))
    alteredInventoryQuantity = inventoryQuantity - orderQuantity
    alteredInventoryValue = inventoryPrice * alteredInventoryQuantity
    orderPrice = inventoryPrice * orderQuantity
    orderTotal += orderPrice
    inventoryItems.append(inventoryID)
    pricePerItem[inventoryID] = inventoryPrice
    quantityPerItem[inventoryID] = orderQuantity
    totalPerItem[inventoryID] = orderPrice
    print(f"Inventory Items: {inventoryItems}")
    print(f"Price Per Item: {pricePerItem}")
    print(f"Quantity Per Item: {quantityPerItem}")
    print(f"Total Per Item: {totalPerItem}")
    print(f"Order Total: {orderTotal}")
#    inventoryPrice = float(obtainInventoryItem(inventoryID))
#    orderQuantity = float(input("Enter the order quantity: "))
#    orderPrice = inventoryPrice * orderQuantity
#    orderTotal += orderPrice
#    print(orderTotal)

conn.close
