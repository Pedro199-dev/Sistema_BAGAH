from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def events(request):
    return render(request, "core/events.html")

def services(request):
    return render(request, "core/services.html")

def products(request):
    return render(request, "core/products.html")
