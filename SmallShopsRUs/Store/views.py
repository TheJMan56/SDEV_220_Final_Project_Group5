from django.shortcuts import render
from .models import Inventory,Users,Orders

def Shop(request):
    inventory = Inventory.objects.all()
    return render(request, "store/shop.html", {"inventory": inventory})
    