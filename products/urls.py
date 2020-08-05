from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('single/<int:pk>', views.productsdetail, name="productsdetail"),
    
]