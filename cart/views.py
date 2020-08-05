from django.http import HttpResponse
from django.shortcuts import render

from carton.cart import Cart
from carton.tests.models import ProductCart


def add(request):
    cart = Cart(request.session)
    product = ProductCart.objects.get(id=request.GET.get('id'))
    cart.add(product, price=product.price)
    return HttpResponse("Added")


def remove(request):
    cart = Cart(request.session)
    product = ProductCart.objects.get(id=request.GET.get('id'))
    cart.remove(product)
    return HttpResponse("Removed")


def show(request):
    return render(request, 'shopping/show-cart.html')
