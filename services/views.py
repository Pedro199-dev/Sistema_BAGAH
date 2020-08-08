from django.shortcuts import render
from products.models import Product
from .models import Service

# Create your views here.

def services(request):
    services = Service.objects.all()
    products = Product.objects.all()
    return render(request, "services/services.html", {'products':products,'services': services})