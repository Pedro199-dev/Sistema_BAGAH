from django.shortcuts import render
from .models import Product
# Create your views here.
def products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products':products})

def productsdetail(request):
    products = Product.objects.all()
    return render(request, "products/single.html", {'products':products})

def checkout(request):
    return render(request, "products/checkout.html")

def payment(request):
    return render(request, "products/payment.html")