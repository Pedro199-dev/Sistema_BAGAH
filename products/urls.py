from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('single/<int:pk>', views.productsdetail, name="productsdetail"),
    path('checkout/', views.checkout, name="checkout"),
    path('payment/', views.payment, name="payment"),
    
]