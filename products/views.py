from django.shortcuts import render
from .models import Product
# Create your views here.
def products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products':products})

def productsdetail(request):
    products = Product.objects.all()
    return render(request, "products/single.html", {'products':products})