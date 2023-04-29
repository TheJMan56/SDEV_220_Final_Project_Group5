inventory = {}
ID = 1

add = int(input("How many seperate items will you be adding to the inventory: "))

for i in range(add):
    inventoryName = input("Enter the name of item {}: ".format(i+1))
    department = input("Enter the department: ")
    inventoryPrice = int(input("Enter the price: "))
    inventoryQuantity = int(input("Enter the quantity: "))

    for j in range(inventoryQuantity):
        item_id = "{:02d}".format(ID)
        inventory[item_id] = {'Item': inventoryName, 'Department': department, 'Price': inventoryPrice}
        ID += 1

print("Inventory:")
for key, value in inventory.items():
    print("ID={id}, Item={item}, Department={department}, Price={price}".format(id=key, item=value['Item'], department=value['Department'], price=value['Price']))