from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Inventory(models.Model):
    inventoryID = models.IntegerField(primary_key = True)
    inventoryName = models.CharField(max_length = 80)
    department = models.CharField(max_length = 80)
    inventoryPrice = models.FloatField()
    inventoryQuantity = models.FloatField()
    inventoryValue = models.FloatField()
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Inventory'
        db_table = "Inventory"
        ordering = ("-added",)
        
class Users(models.Model):
    userID = models.IntegerField(primary_key = True)
    userName = models.CharField(max_length = 80)
    email = models.CharField(max_length = 80)
    loginPassword = models.CharField(max_length = 40)
    creditCard = models.CharField(max_length = 16)
    city = models.CharField(max_length = 80)
    state = models.CharField(max_length = 80)
    country = models.CharField(max_length = 80)
    address = models.CharField(max_length = 80)
    phone =  models.CharField(max_length = 10)
    
    class Meta:
        verbose_name_plural = 'Users'
        db_table = "Users"
        
class Orders(models.Model):
    orderID = models.IntegerField(primary_key = True)
    userID = models.ForeignKey(Users, on_delete = models.CASCADE)
    creditCard = models.CharField(max_length = 16)
    city = models.CharField(max_length = 80)
    state = models.CharField(max_length = 80)
    country = models.CharField(max_length = 80)
    address = models.CharField(max_length = 80)
    items = models.CharField(max_length = 255)
    pricePerItem = models.CharField(max_length = 255)
    quantityPerItem = models.CharField(max_length = 255)
    costPerItem = models.CharField(max_length = 255)
    originalQuantityPerItem = models.CharField(max_length = 255)
    originalValuePerItem = models.CharField(max_length = 255)
    alteredQuantityPerItem = models.CharField(max_length = 255)
    alteredValuePerItem = models.CharField(max_length = 255)
    totalCost = models.FloatField()
    orderDate = models.DateField()
    
    class Meta:
        verbose_name_plural = 'Orders'
        db_table = "Orders"
