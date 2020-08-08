from django.shortcuts import render
from products.models import Product
from blog.models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all()
    products = Product.objects.all()
    return render(request, "core/index.html", {'products':products, 'posts': posts})






