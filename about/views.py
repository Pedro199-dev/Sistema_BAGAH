from django.shortcuts import render
from .models import About
from products.models import Product
# Create your views here.
def about(request):
    abouts = About.objects.all()
    products = Product.objects.all()
    return render(request, "about/about.html", {'products':products, 'abouts': abouts})