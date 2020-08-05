from django.shortcuts import render
from carton.tests.models import ProductCart
# Create your views here.


def index(request):
    products = ProductCart.objects.all()
    return render(request, "core/index.html", {'products':products})

def about(request):
    return render(request, "core/about.html")





