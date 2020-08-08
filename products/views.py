from django.shortcuts import render, get_object_or_404
from .models import Product, Category
# Create your views here.
def products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products':products})

def productsdetail(request, product_id):
    products = Product.objects.all()
    product = get_object_or_404(Product, id=product_id)
    return render(request, "products/single.html", {'products':products,'product':product})

def checkout(request):
    return render(request, "products/checkout.html")

def payment(request):
    return render(request, "products/payment.html")

def category(request, category_id):
    products = Product.objects.all()
    category = get_object_or_404(Category, id=category_id)
    return render(request, "products/category.html", {'products':products, 'category':category})