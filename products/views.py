from django.shortcuts import render
from carton.tests.models import ProductCart
# Create your views here.
def products(request):
    products = ProductCart.objects.all()
    return render(request, "products/products.html", {'products':products})

def productsdetail(request):
    products = ProductCart.objects.all()
    return render(request, "products/single.html", {'products':products})