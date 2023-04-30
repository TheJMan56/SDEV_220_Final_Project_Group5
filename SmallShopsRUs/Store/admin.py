from django.contrib import admin
from .models import Inventory, Users, Orders

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ["inventoryID", "inventoryName", "department", "inventoryPrice", "inventoryQuantity", "inventoryValue"]
    list_filter = ["inventoryID","inventoryPrice", "inventoryQuantity"]
    list_editable = ["inventoryPrice", "inventoryQuantity", "inventoryValue"]

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["userID", "userName", "city", "state", "address"]
    list_filter = ["userID",]

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ["orderID", "address", "items", "quantityPerItem", "totalCost", "orderDate"]
    list_filter = ["orderDate", "orderID"]
    
    
    