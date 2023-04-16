import sqlite3

conn = sqlite3.connect('Inventory.db')
curs = conn.cursor()
ins = 'INSERT INTO Inventory (inventoryID, inventoryName, department,\
      inventoryPrice, inventoryQuantity, inventoryValue) \
      VALUES (?, ?, ?, ?, ?, ?)'

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

while True:
    inventoryID = input("Enter the inventory ID: ")
    if inventoryID == "":
        break
    inventoryName = input("Enter the inventory name: ")
    department = input("Enter the department: ")
    while True:
        inventoryPrice = input("Enter the inventory price: ")
        if isfloat(inventoryPrice) == True:
            inventoryPrice = float(inventoryPrice)
            break
    while True:
        inventoryQuantity = input("Enter the inventory quantity: ")
        if isfloat(inventoryQuantity) == True:
            inventoryQuantity = float(inventoryQuantity)
            break
    inventoryValue = inventoryPrice * inventoryQuantity
    curs.execute(ins, (inventoryID, inventoryName, department, \
                       inventoryPrice, inventoryQuantity, inventoryValue))
    conn.commit()

