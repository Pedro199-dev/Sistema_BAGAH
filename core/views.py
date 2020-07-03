from django.shortcuts import render
from products.models import Product
# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, "core/index.html", {'products':products})

def about(request):
    return render(request, "core/about.html")

def events(request):
    return render(request, "core/events.html")

def services(request):
    return render(request, "core/services.html")


